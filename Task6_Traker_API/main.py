# def main():
#     print("Hello from fastdca-p1!")


# if __name__ == "__main__":
#     main()

# main.py
from fastapi import FastAPI, HTTPException
from models import User, UserCreate, Task, TaskCreate, TaskUpdateStatus
from typing import Dict, List

app = FastAPI()

# 🌐 In-memory databases
USERS: Dict[int, User] = {}
TASKS: Dict[int, Task] = {}

# ID counters
user_id_seq = 1
task_id_seq = 1

@app.post("/users/", response_model=User)
def create_user(user_data: UserCreate):
    global user_id_seq
    user = User(id=user_id_seq, **user_data.dict())
    USERS[user_id_seq] = user
    user_id_seq += 1
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail ="User not found")
    return user

@app.post("/tasks/", response_model=Task)
def create_task(task_data: TaskCreate):
    global task_id_seq
    if task_data.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    task = Task(
        id=task_id_seq,
        status="pending",
        **task_data.dict()
    )
    TASKS[task_id_seq] = task
    task_id_seq += 1
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status_data: TaskUpdateStatus):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.status = status_data.status
    TASKS[task_id] = task
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_tasks_for_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_tasks = [task for task in TASKS.values() if task.user_id == user_id]
    return user_tasks
