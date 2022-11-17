from typing import Union

from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: Union[str, None] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []

#     class Config:
#         orm_mode = True


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: Union[str, None] = None


# class AdminBase(BaseModel):
#     name: str
#     username: str
#     email: str
#     role: int


# class AdminCreate(AdminBase):
#     password: str


# class Admin(AdminBase):
#     id: int

#     class Config:
#         orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class Admin(BaseModel):
    username: str
    email: Union[str, None] = None
    name: Union[str, None] = None
    role: Union[int, None] = None

    class Config:
        orm_mode = True


class AdminInDB(Admin):
    password: str
