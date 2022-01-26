from sqlalchemy import Column, Integer, String

from DatabaseConnector import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return "User{ id:%s name:%s}" % (self.id, self.name)

    def __str__(self):
        return "User{ id:%s name:%s}" % (self.id, self.name)
