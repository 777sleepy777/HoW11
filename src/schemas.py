from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, PastDate


class EmailModel(BaseModel):
    email: EmailStr = Field(max_length=25)


class EmailResponse(EmailModel):
    id: int

    class Config:
        orm_mode = True


class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=100)
    birthday: PastDate
    description: str = Field(max_length=250)


class ContactModel(ContactBase):
    emails: List[int]


##class ContactUpdate(ContactModel):
    #done: bool


#class ContactStatusUpdate(BaseModel):
   # done: bool


class ContactResponse(ContactBase):
    id: int
    #created_at: datetime
    emails: List[EmailResponse]

    class Config:
        orm_mode = True
