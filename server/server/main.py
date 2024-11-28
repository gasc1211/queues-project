import os
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from .models.UserLogin import UserLogin
from .models.UserSignup import UserSignup
from .controllers.firebase import register_user_firebase, login_user_firebase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

if __name__=="__main__":
  __host__ = os.getenv("HOST")
  __port__ = int(os.getenv("PORT"))

  def dev():
    """ Launched with 'poetry run dev' at root level """
    uvicorn.run("server.main:app", host=__host__, port=__port__, reload=True)