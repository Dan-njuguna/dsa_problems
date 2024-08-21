#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

details = {
    "user": "root",
    "password": "XXXXXXXX",
    "host": "127.0.0.1",
    "database": "test",
}

# Connection string
connect_string = f"mysql+pymysql://{details['user']}:{details['password']}@{details['host']}/{details['database']}"

# Create an engine
engine = create_engine(connect_string)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarsative class definitions
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

# Create all tables in the engine
Base.metadata.create_all(engine)

session = Session()

new_user = User(name="Joe Karanja", fullname="Joe Njoroge Karanja", nickname="Jowie")
session.add(new_user)
session.commit()

users = session.query(User).all()

for user in users:
    print(user.name, user.fullname, user.nickname)

engine.close()