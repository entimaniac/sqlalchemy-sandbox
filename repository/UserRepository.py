from DatabaseConnector import Session
from model.User import User


def create_user(user: User, session):
    session.add(user)
    session.commit()


def get_by_id(id: int, session):
    return session.query(User).get(id)


def get_all(session):
    return session.query(User).all()
