import frontend
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from status_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from decouple import config


# format _id
def default(item):
    if isinstance(item, ObjectId):
        return str(item)


app = FastAPI()


# connect to our Database and settings (credentials)
user_name = config('DB_USER_NAME')
user_password = config('DB_PASSWORD')
client = pymongo.MongoClient(
    f"mongodb+srv://{user_name}:{user_password}@kobo.k0upp8i.mongodb.net/")
db = client.nicegui
tododb = db.todo

# MODELS -


class Todo(BaseModel):
    d_todo: str
    created: datetime = datetime.utcnow()


# update blog todo
class UpdateTodo(Todo):
    d_todo: str


"""
Just a random route --- 
"""


@app.get('/', status_code=HTTP_200_OK)
def read_root():
    return {'message': 'This is a simple todo API with with FastAPI and MongoDB'}


"""
Create new todo
"""


@app.post('/todo', status_code=HTTP_201_CREATED)
async def add_post(post: Todo):
    tododb.insert_one(post.model_dump())
    return {'message': "Todo successfully created"}


"""
To get all todos
"""


@app.get("/todos", status_code=HTTP_200_OK)
async def all_post():
    all_todo = tododb.find().sort("created", -1)
    data = []
    for todo in all_todo:
        data.append(
            {'todo_id':  default(todo["_id"]),
                'todo': todo['d_todo'],
                'created': todo['created'].strftime("%b %d, %Y")
             }
        )
    return data


"""
To get a single todo - todo filtered by id --- 
"""


@app.get("/post/{todo_id}", status_code=HTTP_200_OK)
async def single_post(todo_id: str):
    singleTodo = tododb.find_one({'_id': ObjectId(todo_id)})
    if not singleTodo:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Invalid query")
    data = {
        'todo_id': default(singleTodo["_id"]),
        'todo': singleTodo['d_todo'],
        'created': singleTodo['created'].strftime("%b %d, %Y")
    }
    return data


"""
To delete a single todo - todo filtered by id ------
"""


@app.delete("/todos/{todo_id}", status_code=HTTP_200_OK)
async def delete_todo(todo_id: str):
    result = tododb.delete_one({'_id': ObjectId(todo_id)})
    if result.deleted_count == 1:
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                        detail="Todo not found")


"""
To update a single todo - todo filtered by id --------
"""


@app.put('/todos/{todo_id}', status_code=HTTP_200_OK)
async def add_post(post: UpdateTodo, todo_id: str):
    singleTodo = tododb.find_one({'_id': ObjectId(todo_id)})
    if not singleTodo:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Todo not found")
    d_todo = post.d_todo
    tododb.update_one({'_id': ObjectId(todo_id)}, {"$set": {
        "d_todo": d_todo,
    }}),
    return {'message': "Todo successfully updated"}


# -----INITIAL--
frontend.init(app)
if __name__ == '__main__':
    print('Start app with  "uvicorn" command as shown in FastAPI Documentation')


"""
# JUST RUNNING THE APP
uvicorn app:app --reload

# -- RUN THE APP WITH SPECIFIED HOST AND PORT
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

# ----- STATUS CODES
1. Create (POST):
   - 201 Created: The resource has been successfully created.

2. Read (GET):
   - 200 OK: The request was successful.

3. Update (PUT/PATCH):
   - 200 OK: The request was successful.
   - 204 No Content: The request was successful, and there is no additional content to send.

4. Delete (DELETE):
   - 200 OK: The request was successful.
   - 204 No Content`: The request was successful, and there is no additional content to send.
"""
