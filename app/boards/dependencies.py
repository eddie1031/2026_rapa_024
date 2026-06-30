from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.boards.repository import BoardRepository
from app.boards.service import BoardService
from app.dependencies.common import get_session


def get_board_repository(
        session: AsyncSession = Depends(get_session)
) -> BoardRepository:
    return BoardRepository(session)


def get_board_service(
    board_repository: BoardRepository = Depends(get_board_repository),
    session: AsyncSession = Depends(get_session)
) -> BoardService:
    return BoardService(session, board_repository)


