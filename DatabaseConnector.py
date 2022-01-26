from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:pwd0123456789@localhost:5432/postgres', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
