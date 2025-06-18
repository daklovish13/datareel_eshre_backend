from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  
import os

# Load from env or use default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://video_db_nl3t_user:TrHs5IAE1s3ZLH51RD7m2uCrhsxytnjD@dpg-d197eevfte5s73c38icg-a.oregon-postgres.render.com/video_db_nl3t")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
