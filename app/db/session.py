from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.database import engine

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

