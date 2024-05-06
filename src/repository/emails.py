from typing import List

from sqlalchemy.orm import Session

from src.database.models import Email
from src.schemas import EmailModel


async def get_emails(skip: int, limit: int, db: Session) -> List[Email]:
    return db.query(Email).offset(skip).limit(limit).all()


async def get_email(email_id: int, db: Session) -> Email:
    return db.query(Email).filter(Email.id == email_id).first()


async def create_email(body: EmailModel, db: Session) -> Email:
    email = Email(email=body.email)
    db.add(email)
    db.commit()
    db.refresh(email)
    return email


async def update_email(email_id: int, body: EmailModel, db: Session) -> Email | None:
    email = db.query(Email).filter(Email.id == email_id).first()
    if email:
        email.email = body.email
        db.commit()
    return email


async def remove_email(email_id: int, db: Session)  -> Email | None:
    email = db.query(Email).filter(Email.id == email_id).first()
    if email:
        db.delete(email)
        db.commit()
    return email
