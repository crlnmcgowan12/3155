from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_USER = "root" 
DATABASE_PASSWORD = "Carnick12$"
DATABASE_HOST = "localhost"
DATABASE_NAME = "sandwich_maker_api"

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()