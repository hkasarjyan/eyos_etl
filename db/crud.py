import datetime
from datetime import datetime

from sqlmodel import Session, insert, select

from db import engine
from models import Country, Stores


def get_country_by_name(name):
    with Session(engine) as session:
        statement = select(Country).where(Country.country_name == name)
        results = session.exec(statement)
        country = results.one()
        return country


def add_store(store: Stores):
    with Session(engine) as session:
        session.add(store)
        session.commit()
        session.refresh(store)
        store.store_code = store.country_code + str(store.store_id)
        session.add(store)
        session.commit()
        session.refresh(store)
        return store
