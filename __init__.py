from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from model.User import User
from repository.UserRepository import get_by_id, create_user, get_all

engine = create_engine('postgresql://postgres:pwd0123456789@localhost:5432/postgres')
Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()

print("getting user:")
the_user = get_by_id(1, session)
print(the_user)


print("creating user:")
new_user = User()
new_user.name = "new test"
print(new_user)

create_user(new_user, session)

print(new_user)



print("getting all:")
users = get_all(session)
print(users)
