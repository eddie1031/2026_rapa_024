from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.posts.models import Post

class PostRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, post: Post) -> Post:
        self.session.add(post)
        await self.session.flush()
        return post

    async def find_by_id(self, target_id: int) -> Optional[Post]:
        query = select(Post).where(Post.id == target_id)

        result = await self.session.execute(query)
        
        return result.scalar_one_or_none()

    async def delete(self, target: Post) -> None:
        await self.session.delete(target)
        await self.session.flush()