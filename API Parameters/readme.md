
# What are API Parameters?
API Parameters are pieces of information that you send with a request to an API to help it understand what you want.

They act like extra instructions, telling the API:

"Give me this specific data" or "Do this action in a specific way."



# Types of API Parameters with Definitions:

## 1. Path Parameters
Definition:
Yeh parameters URL ke andar directly hote hain aur kisi specific resource ko identify karte hain.

Example:
/users/5 → Yahaan 5 user ki ID hai.

Use: Jab kisi specific item ya ID ko access karna ho.

## 2. Query Parameters
Definition:
Yeh parameters URL ke end mein ? ke baad likhe jaate hain aur optional hote hain. Yeh filters ya search ke liye use hote hain.

Example:
/search?item=book&price=low

Use: Jab tum filter, sort ya search karna chah rahi ho.

## 3. Request Body Parameters
Definition:
Yeh parameters request ke body (andar) mein hote hain, aksar JSON format mein. Yeh tab use hote hain jab tum form ya data bhejna chahti ho.

Example:

json
Copy
Edit
{
  "name": "Maryam",
  "email": "maryam@gmail.com"
}
Use: Jab data create ya update karna ho (jaise signup form).

## 4. Header Parameters
Definition:
Yeh request ke headers mein hote hain. Yeh aksar authentication ya metadata ke liye use hote hain.

Example:
Authorization: Bearer your_token_here

Use: Jab tumhe API ko secure banana ho (jaise login token dena).


## 5. Cookie Parameters
Definition:
Yeh parameters browser ke cookies se aate hain aur aksar user session ya preferences ko store karne ke liye use hote hain.

Example:
session_id=XYZ123

Use: Jab tum user ki state ya session track karna chahti ho.

# In this step, we'll focus on the first two types and how to add validation to them. Take the code from last step and update it with following examples or quickly setup

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi[standard]"
```

## Enhanced Path Parameter Validation

FastAPI offers the `Path()` function to add constraints and metadata to path parameters:

Update main.py

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  # ... means the parameter is required
        title="The ID of the item",
        description="A unique identifier for the item",
        ge=1  # greater than or equal to 1
    )
):
    return {"item_id": item_id}
```

Run the server and try it out in docs:

```bash
fastapi dev main.py
```

## Enhanced Query Parameter Validation

Similarly, the `Query()` function adds validation to query parameters:

Add a new route:

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,  # Default value is None (optional parameter)
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),  # Greater than or equal to 0
    limit: int = Query(10, le=100)  # Less than or equal to 100
):
    return {"q": q, "skip": skip, "limit": limit}
```

## Using Multiple Parameters Together

You can combine different types of parameters in a single endpoint:

```python
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

app = FastAPI()

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result
```

## Complete Example: main.py

Here's the complete code with various parameter types and validations.

```python
from fastapi import FastAPI, Path, Query, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  # ... means the parameter is required
        title="The ID of the item",
        description="A unique identifier for the item",
        ge=1  # greater than or equal to 1
    )
):
    return {"item_id": item_id}

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,  # Default value is None (optional parameter)
        title="Query string",
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(0, ge=0),  # Greater than or equal to 0
    limit: int = Query(10, le=100)  # Less than or equal to 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result
```

## Running the Application

1. Save the above code as `main.py` in the `03_api_parameters` directory.
2. Install the required dependencies:
   ```bash
   uv add "fastapi[standard]"
   ```
3. Run the FastAPI application:
   ```bash
   fastapi dev main.py
   ```
4. Open the interactive documentation at `http://localhost:8000/docs` to explore and test the endpoints.

## Key Points to Remember

- Use `Path()` for validating path parameters
- Use `Query()` for validating query parameters
- Both `Path()` and `Query()` support various validation options:
  - `ge`, `gt`, `le`, `lt` for numerical constraints
  - `min_length`, `max_length` for string length
  - `regex` or `pattern` for pattern matching
  - `enum` for restricting to a set of values
- FastAPI will automatically validate all parameters according to your specifications
- When validation fails, FastAPI returns a 422 Unprocessable Entity status code with detailed error information

---

In the next step, we'll learn about dependency injection in FastAPI, which enables more modular and reusable code.


