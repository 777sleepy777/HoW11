from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact, Email
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    emails = db.query(Email).filter(Email.id.in_(body.emails)).all()
    contact = Contact(name=body.name, surname=body.surname, birthday=body.birthday,
                      description=body.description, emails=emails)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        emails = db.query(Contact).filter(Contact.id.in_(body.emails)).all()
        contact.name = body.name
        contact.description = body.description
        contact.surname = body.surname
        contact.birthday = body.birthday
        contact.emails = emails
        db.commit()
    return contact


