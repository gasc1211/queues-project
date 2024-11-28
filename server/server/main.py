from typing import Union
from fastapi import FastAPI, Request, Response

from models.UserSignup import UserSignup
from models.UserLogin import UserLogin
from controllers.firebase import register_user_firebase, login_user_firebase

app = FastAPI()

@app.get("/")
def read_root():
  return "Hello from FastAPI!"


@app.post("/signup")
async def signup(user: UserSignup):
  """ Signup for the application """
  return await register_user_firebase(user)

@app.post("/login")
async def login(user: UserLogin):
  """ Login into the application"""
  return await login_user_firebase(user)

@app.get("/user")
async def getUser(req: Request, res: Response):
  """ Get user data"""
  pass