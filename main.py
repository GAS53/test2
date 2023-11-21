import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.main_router import router
import settings
from db_func.models import Base
from db_func.db_utils import engine


Base.metadata.create_all(engine)

app = FastAPI(
    debug=settings.DEBUG,
    title='Powerz api',
    description='Open Api документация',
    contact=dict(email='gas53@bk.ru')
)

if settings.DEBUG:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(router)


if settings.DEBUG:
    if __name__ == "__main__":
        uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.IS_RELOAD_SERVER)
else:
    if __name__ == "__main__":
        uvicorn.run("main:app", workers=settings.WORKERS, host=settings.HOST, reload=settings.IS_RELOAD_SERVER, port=settings.PORT)

