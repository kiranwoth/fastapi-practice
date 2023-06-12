from enum import Enum
from fastapi import FastAPI

class UserID (str, Enum):
    kiran = "kiran"
    cherian = "cherian"
    wotherspoon = "wotherspoon"

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: UserID):
    if user_id is UserID.kiran:
        return {"user_id": user_id, "message": "thats my name!"}
    
    if user_id.value == "cherian":
        return {"user_id": user_id}
    
    if user_id is UserID.wotherspoon:
        return {"user_id": user_id, "message": "thats my last name!"}
    
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
