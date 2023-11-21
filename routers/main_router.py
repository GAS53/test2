from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from dependences import get_db
from schemas import One_task
from db_func import db_utils

router = APIRouter(prefix='/test')

@router.post('/tasks/')
async def create_task(task: One_task, db: Session=Depends(get_db)):
    task = task.model_dump()
    res = await db_utils.create_task(task, db)
    return JSONResponse(content={"message": "ok"}, status_code=200)


@router.get('/tasks/')
async def get_all_tasks(db: Session=Depends(get_db)):
    res = await db_utils.get_all_tasks(db)
    return res


@router.get('/tasks/<task_id>')
async def get_all_tasks(task_id, db: Session=Depends(get_db)):
    await db_utils.get_one_tasks(task_id, db)
    return res


@router.put('/tasks/<task_id>')
async def put_task(task_id: int, task: One_task, db: Session=Depends(get_db)):
    task = task.model_dump()
    await db_utils.put_one_tasks(task_id, task, db)
    return JSONResponse(content={"message": "ok"}, status_code=200)


@router.delete('/tasks/<task_id>')
async def put_task(task_id: int, db: Session=Depends(get_db)):
    await db_utils.del_one_tasks(task_id, db)
    return JSONResponse(content={"message": "ok"}, status_code=204)