from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.boards.models import Board

from typing import Optional, List


class BoardRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, board: Board) -> Board:
        self.session.add(board)
        await self.session.flush()
        return board

    async def find_by_id(self, board_id: int) -> Optional[Board]:
        query = select(Board).where(Board.id == board_id)
        result = await self.session.execute(query)
        find_board = result.scalar_one_or_none()
        return find_board

    async def find_all(self):
        results = await self.session.execute(select(Board))
        return results.scalars().all()


    async def delete(self, board: Board) -> None:
        await self.session.delete(board)
        await self.session.flush()



