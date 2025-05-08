


# 1- What is FastAPI?

**FastAPI** ek modern aur powerful web framework hai jo Python mein APIs banane ke liye use hoti hai.  
Ye specially un logon ke liye bohot helpful hai jo Python already jaante hain.

### 🔹 Key Features:

-  **Lightning fast** — Python ke other frameworks se zyada fast hai (almost like Node.js and Go).
-  **Beginner-friendly** — Agar aapko Python aati hai to FastAPI seekhna bohot easy hai.
-  **Modern features** — Type hints, async programming, aur automatic API docs jaise latest features ko support karta hai.
- 📄 **Auto Documentation** — Swagger UI aur ReDoc ke through docs khud ban jati hain — bina extra effort ke!

> 🧠 **Simple words mein**:  
> FastAPI aapki Python code ko ek professional API mein badal deta hai — fast, smart aur developer-friendly.

---

# 2- What is Uvicorn (UV)?

**Uvicorn** ek ASGI server hai jo FastAPI jaise asynchronous frameworks ko run karta hai.

### 🔹 Key Features:

-  **ASGI support** — Async aur WebSockets jaise modern protocols ko handle karta hai.
- ⚙ **Fast and Lightweight** — Bohot chhota aur efficient server hai, jo performance ko top level par rakhta hai.
-  **Runs your app** — Ye aapke FastAPI app ko browser ya kisi client ke saamne run karta hai.

> 🚗 **Easy example**:  
> Agar FastAPI ek car hai to Uvicorn uska engine hai — bina engine ke car nahi chalegi.



# **Step 1: Project Setup with FastAPI + Uvicorn**

### 📁 1. Project Folder banao aur usme jao:

```bash
uv init fastdca-p1
cd fastdca-p1
```

### 🐍 2. Virtual Environment banao aur activate karo:

**Linux/macOS:**

```bash
uv venv
source .venv/bin/activate
```

**Windows:**

```bash
uv venv
.venv\Scripts\activate
```

> ℹ️ Note: Python 3.11+ me PEP 582 ke wajah se kabhi kabhi manual activation zarurat nahi hoti.



# 📦 **Step 2: FastAPI + Uvicorn dependencies install karo**

```bash
uv add "fastapi[standard]"
```

**Yeh install karega:**

* `fastapi`: Web framework
* `uvicorn`: Server to run the app
* `httpx`: For testing APIs



# 🧪 **Step 3: Testing tools add karo (dev dependencies)**

```bash
uv add --dev pytest pytest-asyncio
```

Yeh `pyproject.toml` ko update karega with testing setup.



# 🛠 **Step 4: First API route banao (main.py)**

Create or edit `main.py` file:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```


# **Step 5: Server run karo (dev mode)**

```bash
fastapi dev main.py
```

> 🔄 Ye auto-reload karta hai jab bhi tum code update karo. Sirf **development** ke liye use karo.

**Agar error aaye ya app run na ho to alternate use karo:**

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


# 🌐 **Step 6: Test your API in browser/postman**

* Root URL: `http://localhost:8000`
* Example API: `http://localhost:8000/items/5?q=somequery`
* Swagger Docs: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`



