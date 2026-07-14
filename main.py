from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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
    
class TaskCreate(BaseModel):
    title : str
    
@app.post("/tasks")
def create_task(task : TaskCreate):
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