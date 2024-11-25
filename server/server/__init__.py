import uvicorn

def dev():
  """ Launched with 'poetry run dev' at root level """
  uvicorn.run("server.main:app", host="0.0.0.0", port=3000, reload=True)
