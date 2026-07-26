from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

conn = sqlite3.connect("tasks.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL
)
""")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

if count == 0:
    example_tasks = [
        ("Create Hello server", True),
        ("Root and Health Endpoints", True),
        ("Read list and single task", False)
    ]

    cursor.executemany(
        "INSERT INTO tasks(title, done) VALUES (?, ?)",
        example_tasks
    )
    conn.commit()

class Tasks(BaseModel):
    title : str | None=None
    done : bool | None=None


@app.get("/")
def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    return [
        {
            "id": row["id"],
            "title": row["title"],
            "done": bool(row["done"])
        }
        for row in rows
    ]

@app.get("/tasks/{id}")
def tasks_id(id: int):

    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (id,)
    )

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": task["id"],
        "title": task["title"],
        "done": bool(task["done"])
    }
@app.post("/tasks", status_code=201)
def create_task(task: Tasks):

    if task.title is None or task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    cursor.execute(
        "INSERT INTO tasks(title, done) VALUES(?, ?)",
        (task.title, False)
    )

    conn.commit()

    new_id = cursor.lastrowid

    return {
        "id": new_id,
        "title": task.title,
        "done": False
    }
    
@app.put("/tasks/{id}")
def update_title(id: int, current_task: Tasks):

    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (id,)
    )

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    title = current_task.title if current_task.title is not None else task["title"]
    done = current_task.done if current_task.done is not None else task["done"]

    cursor.execute(
        """
        UPDATE tasks
        SET title=?, done=?
        WHERE id=?
        """,
        (title, done, id)
    )

    conn.commit()

    return {
        "id": id,
        "title": title,
        "done": bool(done)
    }
          
@app.delete("/tasks/{id}")
def delete_task(id: int):

    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (id,)
    )

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (id,)
    )

    conn.commit()

    return {"message": "Task deleted"}
    