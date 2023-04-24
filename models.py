from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import column_property
from sqlalchemy.orm.decl_api import declared_attr
from sqlmodel import Column, Enum, Field, SQLModel, String


class LookupGeog(SQLModel, table=True):
    __tablename__ = "dim_lookup_geog"
    country_id: Optional[int] = Field(default=None, primary_key=True)
    country_code: str = Field(sa_column=Column("country_code", String(100)))
    lvl1: str = Field(
        sa_column=Column("lvl1", String(100)), foreign_key="dim_geog.lvl_code"
    )
    lvl2: str = Field(
        sa_column=Column("lvl2", String(100)), foreign_key="dim_geog.lvl_code"
    )
    lvl3: str = Field(
        sa_column=Column("lvl3", String(100)), foreign_key="dim_geog.lvl_code"
    )


class Geog(SQLModel, table=True):
    __tablename__ = "dim_geog"
    lvl_id: Optional[int] = Field(default=None, primary_key=True)
    lvl_code: str = Field(sa_column=Column("lvl_code", String(100)), unique=True)
    lvl_name: str = Field(sa_column=Column("lvl_name", String(100)))


class Country(SQLModel, table=True):
    __tablename__ = "dim_country"
    country_id: Optional[int] = Field(default=None, primary_key=True)
    country_code: str = Field(sa_column=Column("country_code", String(100)))
    country_name: str = Field(sa_column=Column("country_name", String(100)))


class Stores(SQLModel, table=True):
    __tablename__ = "dim_stores"
    store_id: Optional[int] = Field(default=None, primary_key=True)

    store_code: str = Field(sa_column=Column("store_code", String(100)))
    # @declared_attr
    # def store_code(self):
    #     return column_property(func.my_string(self.country_code + str(self.store_id)))

    def get_store_code(self):
        return self.country_code + str(self.store_id)

    store_name: str = Field(sa_column=Column("store_name", String(100)))
    country_code: str = Field(
        sa_column=Column("country_code", String(100)),
        foreign_key="dim_country.country_name",
    )
    street_name: str = Field(sa_column=Column("street_name", String(100)))
    pin_code: str = Field(sa_column=Column("pin_code", String(100)))
    lvl1_geog: str = Field(sa_column=Column("lvl1_geog", String(100)))
    lvl2_geog: str = Field(sa_column=Column("lvl2_geog", String(100)))
    lvl3_geog: str = Field(sa_column=Column("lvl3_geog", String(100)))
