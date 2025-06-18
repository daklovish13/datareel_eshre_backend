
from database import Base, engine, SessionLocal
from models import Video

# # Create tables
Base.metadata.create_all(bind=engine)

# Sample data
sample_videos = [
   
    Video(avatar_id=3, language="French", video_type="Embryo Grading Explaination", disease="Endometriosis", video_url="http://localhost:8000/static/eshre_demo3.mp4"),
]

# Insert data
db = SessionLocal()
db.add_all(sample_videos)
db.commit()
db.close()

print("✅ Sample videos inserted successfully!")


