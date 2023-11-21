from sqlalchemy.orm import sessionmaker


from db_func.db_utils import engine


DBSession = sessionmaker(bind=engine)

async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()