from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
engine=create_engine("sqlite:///database.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

