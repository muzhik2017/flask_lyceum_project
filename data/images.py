import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Image(SqlAlchemyBase):
    __tablename__ = 'images'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    estate_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("items.id"))
    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    item = orm.relation('Item')
