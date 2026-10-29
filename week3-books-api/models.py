from sqlalchemy import Column, Integer, String

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    auther = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    