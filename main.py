from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from fastapi.staticfiles import StaticFiles
from models import Video
from schemas import VideoFilter
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Video Generation API",
    description="Backend API for video selection and retrieval",
    version="1.0.0",
    docs_url="/docs",         # Swagger UI
    redoc_url="/redoc",       # ReDoc documentation
    openapi_url="/openapi.json"
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.post("/get-video-id")
def get_video_id(payload: VideoFilter, db: Session = Depends(get_db)):
    video = db.query(Video).filter_by(
        avatar_id=payload.avatar_id,
        language=payload.language,
        video_type=payload.video_type,
        disease=payload.disease
    ).first()

    if not video:
        raise HTTPException(status_code=404, detail="Currently video is not available")

    return {
        "video_id": video.id,
        "video_url": video.video_url
    }
