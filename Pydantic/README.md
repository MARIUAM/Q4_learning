

#  Definition of Pydantic 
Pydantic ek Python library hai jo aapko data models banane aur data validate karne mein madad karti hai.
Ye ensure karti hai ke user se milne wala data sahi type ka ho (jaise string, number, list waghera) aur koi galti na ho.

## 🔍 Pydantic Features


| Feature                 | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| **Data validation**     | Automatically checks if data matches the types you declared      |
| **Data parsing**        | Converts data (e.g. from string `"123"` to integer `123`)        |
| **Type hints support**  | Uses Python’s type hints (`int`, `str`, etc.) to validate        |
| **Easy errors**         | Gives helpful error messages when data is invalid                |
| **FastAPI integration** | Works perfectly with FastAPI for API request/response validation |



#  Use Cases:
FastAPI models (request/response)

Validating form or user input

Working with external APIs

Structuring large projects with clean data types



## Step 1: Getting Started with Pydantic

Let’s explore Pydantic with examples before integrating it into our FastAPI app.

Take the last step code as start code or quickly setup a new project using following commands:
```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
```
### 1. Basic Pydantic Model

Create a file named `pydantic_example_1.py`:

```python
from pydantic import BaseModel, ValidationError

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None  # Optional field with default None

# Valid data
user_data = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25}
user = User(**user_data)
print(user)  # id=1 name='Alice' email='alice@example.com' age=25
print(user.model_dump())  # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25}

# Invalid data (will raise an error)
try:
    invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)
```

Run the script:

```bash
uv run python pydantic_example_1.py
```

Output for invalid data:

```
1 validation error for User
id
  value is not a valid integer (type=type_error.integer)
```

### 2. Nested Models

Pydantic supports nested structures, which we’ll use in our FastAPI app. Create `pydantic_example_2.py`:

```python
from pydantic import BaseModel, EmailStr

# Define a nested model


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr  # Built-in validator for email format
    addresses: list[Address]  # List of nested Address models


# Valid data with nested structure
user_data = {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "addresses": [
        {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
        {"street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001"},
    ],
}
user = UserWithAddress.model_validate(user_data)
print(user.model_dump())
```

Output:

```json
{
  "id": 2,
  "name": "Bob",
  "email": "bob@example.com",
  "addresses": [
    { "street": "123 Main St", "city": "New York", "zip_code": "10001" },
    { "street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001" }
  ]
}
```

### 3. Custom Validators

Add a custom validator to ensure the user’s name is at least 2 characters long:

pydantic_example_3.py

```python
from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# Test with invalid data
try:
    invalid_user = UserWithAddress(
        id=3,
        name="A",  # Too short
        email="charlie@example.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    print(e)
```

Output:

```
1 validation error for UserWithAddress
name
  ValueError: Name must be at least 2 characters long
```

### 4. Why Pydantic for DACA?

Pydantic is critical for DACA because:

- **Data Integrity**: Ensures incoming user data and agent responses are valid and type-safe.
- **Complex Workflows**: Supports nested models for agentic AI scenarios (e.g., user messages with metadata, agent responses with context).
- **Serialization**: Seamlessly converts models to JSON for API responses.
- **Error Handling**: Provides clear validation errors, improving debugging in distributed systems.

---

## Step 2: Building a FastAPI Application with Complex Pydantic Models

Let’s build a FastAPI app for a chatbot with a more complex data model, simulating an agentic AI workflow where users send messages with metadata (e.g., timestamps, session IDs).

### Create the Main Application File

Create `main.py`:

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

# Initialize the FastAPI app
app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)

# Complex Pydantic models
class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))


class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata
    tags: list[str] | None = None  # Optional list of tags


class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}

# GET endpoint with query parameters
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info

# POST endpoint for chatting
@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(
            status_code=400, detail="Message text cannot be empty")
    reply_text = f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata()  # Auto-generate timestamp and session_id
    )

```

### Explanation of the Code

1. **Complex Pydantic Models**:

   - `Metadata`: A nested model with a `timestamp` (defaults to current UTC time) and `session_id` (defaults to a UUID).
   - `Message`: The request model, including `user_id`, `text`, `metadata` (nested `Metadata`), and optional `tags`.
   - `Response`: The response model, returning `user_id`, `reply`, and `metadata`.

2. **Endpoint Updates**:
   - The `/chat/` endpoint now accepts a `Message` with nested `Metadata` and returns a `Response` with similar structure.

---

### Run Code

```bash
fastapi dev main.py
```


https://github.com/panaversity/learn-agentic-ai/blob/main/04_daca_agent_native_dev/01_intro_fastapi/02_pydantic_validation/readme.md








![image](https://github.com/user-attachments/assets/f989ad58-2f53-4ede-b36f-51c78c8f942c)



![image](https://github.com/user-attachments/assets/6d8e9e26-8472-4f5c-be32-a15ba06d561b)

