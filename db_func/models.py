from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship, mapped_column, DeclarativeBase
from typing import Optional, List


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    

class Task(Base):
    __tablename__ = 'task'
    title: Mapped[Optional[str]] = mapped_column(String(30))
    description: Mapped[Optional[str]] = mapped_column(String(30))
    status: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.now())

    class Meta:
        from_attributes = True