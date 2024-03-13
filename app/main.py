from fastapi import FastAPI, HTTPException
from app.UserManagement import User, UserRepository, UserNotFound
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class UserInfo(BaseModel):
    username: str
    email: str
    password: str


user_repository = UserRepository()
user_repository.add(User("test_user", "test_user@test.com", "test_password"))
app = FastAPI()

origins = [
    "http://alphahr",
    "http://alphahr:8080",
    "http://alphahr:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def list_users():
    users = user_repository.list_users()
    return users


@app.post("/add")
def add_user(user_info: UserInfo):
    user_repository.add(User(user_info.username, user_info.email, user_info.password))


@app.post("/login")
def login(username: str, password: str):
    user = user_repository.get_user(username)
    token = user.login(password)
    user_repository.update_user(user)
    return token


@app.post("/logout")
def logout(username: str, token: str):
    user = user_repository.get_user(username)
    user.logout(token)
    user_repository.update_user(user)


@app.post("/validate_token")
def validate_token(token: str):
    try:
        user = user_repository.get_user_by_token(token)
        return user
    except UserNotFound:
        raise HTTPException(status_code=401, detail="Invalid token")

