import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.config import setting
from api import router as api_router
from core.model import db_helper, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    
    yield 
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(api_router, prefix=setting.api.prefix)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=setting.run.host,
        port=setting.run.port,
        reload=True,
        )