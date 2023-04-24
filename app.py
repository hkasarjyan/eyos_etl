from sqlmodel import Session, SQLModel
import db

SQLModel.metadata.create_all(db.engine)
