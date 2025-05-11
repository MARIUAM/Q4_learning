# DAY 2

# 1- What is FastAPI?

**FastAPI** ek modern aur powerful web framework hai jo Python mein APIs banane ke liye use hoti hai.  
Ye specially un logon ke liye bohot helpful hai jo Python already jaante hain.

### 🔹 Key Features:

- ⚡ **Lightning fast** — Python ke other frameworks se zyada fast hai (almost like Node.js and Go).
- 👶 **Beginner-friendly** — Agar aapko Python aati hai to FastAPI seekhna bohot easy hai.
- 🧠 **Modern features** — Type hints, async programming, aur automatic API docs jaise latest features ko support karta hai.
- 📄 **Auto Documentation** — Swagger UI aur ReDoc ke through docs khud ban jati hain — bina extra effort ke!

> 🧠 **Simple words mein**:  
> FastAPI aapki Python code ko ek professional API mein badal deta hai — fast, smart aur developer-friendly.

---

# 2- What is uv?

**`uv`** ek fast, secure aur modern package manager hai Python ke liye, jo:

- 🧩 Dependency install karta hai (jaise `pip`)
- 🧪 Virtual environment bana sakta hai (jaise `venv`)
- 📦 `pyproject.toml` file ke through har cheez manage karta hai (jaise `poetry`)
- ⚙️ Dependency resolution bohot tezi se karta hai — C language mein likha gaya hai isliye lightning fast hai ⚡




# FastAPI Project

FastAPI is a modern and high-performance web framework for building APIs with Python. It is designed to be fast, easy to use, and scalable, making it a great choice for both small and large applications.

## Features

- 🚀 Super Fast: Supports asynchronous code using async/await, making it very efficient.
- 🧩 Easy to Use: Uses Python type hints for automatic validation.
- 📄 Auto Docs: Automatically creates interactive API docs (Swagger UI and ReDoc).
- ✅ Great Developer Experience: Clean syntax, helpful error messages, and built-in testing support.


## Setup Instructions

### Step 1: Check Python Version

Make sure Python is installed. Run this:

```bash
python --version
```

### Step 2: Create Project Folder

```bash
uv init fastdca-p1
cd fastdca-p1
```

### Step 3: Create and Activate Virtual Environment

**On macOS/Linux:**

```bash
uv venv
source .venv/bin/activate
```

**On Windows:**

```bash
uv venv
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
uv add "fastapi[standard]"
```

This installs:

- `fastapi`: The main framework
- `uvicorn`: Runs the app
- `httpx`: For testing APIs

### Step 5: Add Testing Tools

```bash
uv add --dev pytest pytest-asyncio
```


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}



 15 changes: 15 additions & 0 deletions15  
fastapi/fastdca-p1/pyproject.toml
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,15 @@
[project]
name = "fastdca-p1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "fastapi[standard]>=0.115.12",
]

[dependency-groups]
dev = [
    "pytest>=8.3.5",
    "pytest-asyncio>=0.26.0",
]
 870 changes: 870 additions & 0 deletions870  
fastapi/fastdca-p1/uv.lock
https://github.com/panaversity/learn-agentic-ai/tree/main/04_daca_agent_native_dev/01_intro_fastapi/01_hello_fastapi

https://medium.com/@maryamsaleem20102001/introduction-to-fastapi-and-uvicorn-with-hello-world-example-f701d85f6fd6
