#  Dependency Injection in FastAPI (Super Easy Guide)

FastAPI aik modern aur high-performance Python web framework hai jo Dependency Injection ko **bohot asaan aur smart** bana deta hai. Ye `README.md` un logon ke liye hai jo simple words me samajhna chahte hain ke DI kya hoti hai, kaise kaam karti hai, aur kaise use karni chahiye.

---

##  What is Dependency Injection?

**Dependency Injection (DI)** aik technique hai jisme common logic (jaise database access, login validation, config files, etc.) ko aik function ya class me define karte hain — aur jab bhi zarurat ho, use kisi bhi endpoint ke andar **inject** kar lete hain.

Ye **code reusability**, **modularity**, aur **clean architecture** ke liye bohot zaroori hota hai.

---

##  Why Use Dependency Injection?

✅ Reusable code  
✅ Clean endpoints  
✅ Test karna easy hota hai (mocking possible hoti hai)  
✅ Application maintain karna asaan ho jata hai  

---

## ⚙️ How Does It Work?

1. Aik **dependency function** banate hain.
2. `Depends()` ya `Annotated` use kar ke us function ko kisi bhi route me inject kar dete hain.
3. FastAPI automatically us function ko call karta hai jab route hit hoti hai.

---

## 🍳 Analogy: Chef & Helper

Sochiye aik chef har dafa market se ingredients la kar cooking kare — time waste hoga.  
Lekin agar aik helper ho jo ingredients ready kar ke de de, to chef sirf cooking kare.  
**Helper = Dependency Function**  
**Chef = API Function (endpoint)**

---

##  Code Examples

### ✅ 1. Basic Dependency

```python
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}

@app.get("/get-simple-goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response
```


# Must chek this medium follow for more 

https://medium.com/p/2635f3ecc8ab/edit
