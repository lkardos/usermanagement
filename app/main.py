from fastapi import FastAPI
from app.UserManagement import User, UserRepository
from pydantic import BaseModel


class UserInfo(BaseModel):
    username: str
    email: str
    password: str


user_repository = UserRepository()
app = FastAPI()


@app.get("/")
def list_users():
    users = user_repository.list_users()
    return users


@app.post("/add")
def add_user(user_info: UserInfo):
    user_repository.add(User(user_info.username, user_info.email, user_info.password))




