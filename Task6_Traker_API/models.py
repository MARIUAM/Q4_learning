# models.py
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class Task(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str] = None
    due_date: date
    status: str

    @validator('due_date')
    def check_due_date(cls, value):
        from datetime import date
        if value < date.today():
            raise ValueError("Due date cannot be in the past.")
        return value

class TaskCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None
    due_date: date

    @validator('due_date')
    def check_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date cannot be in the past.")
        return value

class TaskUpdateStatus(BaseModel):
    status: str

    @validator('status')
    def validate_status(cls, value):
        allowed = ["pending", "in_progress", "completed"]
        if value not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value
