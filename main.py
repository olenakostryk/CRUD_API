from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class Tasks(BaseModel):
    title : str | None=None
    done : bool | None=None
    
tasks = [
   { "id": 1,
    "title": "Create Hello server",
    "done" : True},
    
   { "id": 2,
    "title": "Root and Health Endpoints",
    "done" : True},
    
    {"id": 3,
    "title": "Read list and single task",
    "done" : False
}
]

@app.get("/")
def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def  get_tasks():
    return tasks

@app.get("/tasks/{id}")
def tasks_id(id : int):
    for task in tasks:
        if task["id"] == id:
            return task
        
    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )
    
@app.post("/tasks")
def create_task(task : Tasks):
    if task.title.strip() == "":
        raise HTTPException(
            status_code=404,
            detail="Title cannot be empty"
        )
    
    next_id = len(tasks) +1
    
    new_task ={
        "id": next_id,
        "title" : task.title,
        "done": False
    }
    
    tasks.append(new_task)
    
    return new_task

@app.put("/tasks/{id}")
def update_title(id: int, current_task: Tasks):
    for task in tasks:
        if task["id"] == id:
            if current_task.title is not None:
                task["title"] = current_task.title
            if current_task.done is not None:
                task["done"] = current_task.done
            return task
    raise HTTPException(
            status_code=404,
            detail=f"Unknown {id}"
     )
          
@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return None
    raise HTTPException(
            status_code=404,
            detail=f"Unknown {id}"
     )
    
   