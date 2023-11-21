from sqlalchemy import create_engine

import settings
from db_func import models
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete

from db_func.models import Task

engine = create_engine(f"sqlite:///databases/{settings.DB_PATH}")


async def create_task(task: dict, db: Session):
    task = models.Task(**task)
    db.add(task)
    db.commit()


def convert_one_task(task: Task):
    inner_di = {}
    inner_di['title'] = task.title
    inner_di['description'] = task.description
    inner_di['status'] = task.status
    inner_di['created_at'] = task.created_at
    return inner_di


async def get_all_tasks(db: Session):
    tasks = db.query(Task).all()
    result_task = {}
    if not tasks:
        return None
    for task in tasks:
        result_task[task.id] = convert_one_task(task)
    return result_task


async def get_one_tasks(task_id: int, db: Session):
    task = db.scalar(select(Task).where(Task.id == task_id))
    return convert_one_task(task)


async def put_one_tasks(task_id: int, task: Task, db: Session):
    stmt = update(Task).where(Task.id == task_id).values(**task)
    db.execute(stmt)
    db.commit()


async def del_one_tasks(task_id: int, db: Session):
    stmt = delete(Task).where(Task.id == task_id)
    db.execute(stmt)
    db.commit()