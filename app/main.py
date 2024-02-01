from fastapi import FastAPI
from app.UserManagement import User, UserRepository
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class UserInfo(BaseModel):
    username: str
    email: str
    password: str


user_repository = UserRepository()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
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




