from typing import List, Tuple
from database import get_database

from databases import Database
from fastapi import Depends, FastAPI, HTTPException, Query, status
from database import sqlalchemy_engine, get_database
from models.models import posts, metadata

app = FastAPI()


@app.on_event('startup')
async def startup():
    await get_database().connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event('shutdown')
async def shutdown():
    await get_database().disconnect()


@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: PostCreate, database: Database = Depends(get_database)
) -> PostDB:
    insert_query = posts.insert().values(post.dict())
    post_id = await database.execute(insert_query)
    post_db = await get_post_or_404(post_id, database)
    return post_db


@app.get("/posts")
async def list_posts(
    pagination: Tuple[int, int] = Depends(pagination),
    database: Database = Depends(get_database),
) -> List[PostDB]:
    skip, limit = pagination
    select_query = posts.select().offset(skip).limit(limit)
    rows = await database.fetch_all(select_query)
    results = [PostDB(**row) for row in rows]
    return results


@app.get("/posts/{id}", response_model=PostDB)
async def get_post(post: PostDB = Depends(get_post_or_404)) -> 
PostDB:
return post
