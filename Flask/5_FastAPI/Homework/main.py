import uvicorn
from fastapi import FastAPI
from models import Task, Base, engine, db, TaskBase


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def home():
    return {}


@app.get('/tasks')
async def tasks_list():
    res = []
    tasks = db.query(TaskBase).all()
    for task in tasks:
        res.append(f'task_id: {task.id}, title: {task.title}, description: {task.description}, status: {task.status}')
    return res


@app.get('/tasks/{task_id}')
async def id_tasks_list(task_id: int):
    task = db.query(TaskBase).filter(TaskBase.id == task_id).first()
    if task:
        return f'task_id: {task.id}, title: {task.title}, description: {task.description}, status: {task.status}'
    return 'Task is not exist'


@app.post('/tasks')
async def add_tasks_list(task_nw: Task):
    tasks = db.query(TaskBase).all()
    for task in tasks:
        if task.id == task_nw.id:
            return 'Task already exist'
    new_task = TaskBase(id=task_nw.id, title=task_nw.title, description=task_nw.description, status=task_nw.status)
    db.add(new_task)
    db.commit()
    return "Task is created"


@app.put('/tasks/{task_id}')
async def update_tasks_list(task_id: int, task_up: Task):
    task = db.query(TaskBase).filter(TaskBase.id == task_id).first()
    if task:
        task.title = task_up.title
        task.description = task_up.description
        task.status = task_up.status
        db.commit()
        return 'Task is updated'
    return 'Not task like that'


@app.delete('/tasks/{task_id}')
async def delete_tasks_list(task_id: int):
    task = db.query(TaskBase).filter(TaskBase.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return 'Task is deleted'
    return 'Not task like that'


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level='info')
