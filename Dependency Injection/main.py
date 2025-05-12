from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

# Create FastAPI application instance
app = FastAPI()

# ---------------------------------
# Dependency Injection Example 1: Path Parameter Dependency
# ---------------------------------
# A simple dependency function that takes a username and returns a goal message.
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}

# This path operation uses the `get_goal` dependency to get a goal message for the user.
@app.get("/get-goal")
def get_my_goal(response: Annotated[dict, Depends(get_goal)]):
    return response  # Returns the goal message with the username

# ---------------------------------
# Dependency Injection Example 2: Query Parameters
# ---------------------------------
# A dependency function that checks login credentials from query parameters
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message": "Login Successful"}
    else:
        return {"message": "Login Failed"}

# This path operation uses the `dep_login` dependency to authenticate the user
@app.get("/signin")
def login_api(user: Annotated[dict, Depends(dep_login)]):
    return user  # Returns the message from the login function

# ---------------------------------
# Dependency Injection Example 3: Multiple Dependencies
# ---------------------------------

# First dependency function that adds 1 to the given number
def depfunc1(num: int): 
    num = int(num)
    num += 1
    return num

# Second dependency function that adds 2 to the given number
def depfunc2(num): 
    num = int(num)
    num += 2
    return num

# ---------------------------------
# Example without using dependency injection
# ---------------------------------
# This endpoint manually calls the dependency functions directly within the route handler.
@app.get("/main/{num}")
def get_main(num: int):
    num1 = depfunc1(num)  # Calls depfunc1 manually
    num2 = depfunc2(num)  # Calls depfunc2 manually
    total = num + num1 + num2  # Adds the numbers together
    return f"Pakistan {total}"  # Returns the result

# ---------------------------------
# Example with using dependency injection
# ---------------------------------
# This endpoint uses FastAPI's Dependency Injection system to handle dependencies.
@app.get("/main_dependency/{num}")
def get_main(num: int, num1: Annotated[int, Depends(depfunc1)], num2: Annotated[int, Depends(depfunc2)]):
    total = num + num1 + num2  # Adds the numbers together, but dependencies are injected
    return f"Pakistan {total}"  # Returns the result

# ---------------------------------
# Comprehensive Example: Dependency Injection with Classes
# ---------------------------------
# Example: Retrieving blog and user details using class-based dependencies

# Sample data for blogs and users
blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mohammed"
}

# A class that handles fetching objects from the given data model (either blogs or users)
class GetObjectOr404():
    def __init__(self, model) -> None:
        self.model = model  # The model can be blogs or users

    # When called, this class fetches the object by its id and raises an error if not found
    def __call__(self, id: str):
        obj = self.model.get(id)  # Attempts to fetch the object from the model
        if not obj:
            # If object is not found, raise a 404 error with a message
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj  # Return the found object

# Create dependencies for blogs and users using the GetObjectOr404 class
blog_dependency = GetObjectOr404(blogs)
user_dependency = GetObjectOr404(users)

# ---------------------------------
# Endpoint to fetch blog details using dependency injection
# ---------------------------------
@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name  # Returns the blog name for the given ID

# ---------------------------------
# Endpoint to fetch user details using dependency injection
# ---------------------------------
@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name  # Returns the user name for the given ID