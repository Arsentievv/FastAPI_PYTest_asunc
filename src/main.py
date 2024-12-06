import contextlib

from fastapi import FastAPI

from config import get_settings
from data_base.db_connect import session_manager

settings = get_settings()


def init_app(init_db=True):
    lifespan = None

    if init_db:
        session_manager.init(settings.postgres.get_db_uri)

        @contextlib.asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if session_manager._engine is not None:
                await session_manager.close()

        server = FastAPI(title="FastAPI PYTest async", lifespan=lifespan)

        # register routers here

        return server


app = init_app()
