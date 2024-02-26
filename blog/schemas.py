from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

#Response Model
class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser