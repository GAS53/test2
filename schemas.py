from pydantic import BaseModel


class One_task(BaseModel):
    title: str
    description: str
    status: bool