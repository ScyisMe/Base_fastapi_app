from typing import AsyncGenerator

from core.config import setting

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
    
)
class DatabesaHelper:
    def __init__(
        self,
        url: str,
        echo: bool,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    async def dispose(self):
        await self.engine.dispose()
    
    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

db_helper = DatabesaHelper(
    url=str(setting.db.url),
    echo=setting.db.echo,
    echo_pool=setting.db.echo_pool,
    pool_size=setting.db.pool_size,
    max_overflow=setting.db.max_overflow,
)