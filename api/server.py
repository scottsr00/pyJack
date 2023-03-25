from fastapi import FastAPI
from .. import blackjack

app = FastAPI()
    
@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/user/{username}")
def profile(username):
    return f'{username}\'s profile'

@app.get("/play")
def play():
    return {"return code": blackjack.Start()}
