from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Trainer API")

class UserIn(BaseModel):
    name: str

users: dict[int, dict] = {}
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def list_users():
    return list(users.values())

@app.post("/users", status_code=201)
def create_user(body: UserIn):
    global next_id
    user = {"id": next_id, "name": body.name}
    users[next_id] = user
    next_id += 1
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(404, "User not found")
    return users[user_id]
