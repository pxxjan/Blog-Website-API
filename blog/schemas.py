from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str


#Response Model
class ShowBlog(Blog):
    pass


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str