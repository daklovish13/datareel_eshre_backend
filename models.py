from sqlalchemy import Column, Integer, String
from database import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    avatar_id = Column(Integer, index=True)
    language = Column(String, index=True)
    video_type = Column(String, index=True)
    disease = Column(String, index=True)
    video_url = Column(String)
