from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from fastapi.staticfiles import StaticFiles
from models import Video
from schemas import VideoFilter
from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI(
#     title="Video Generation API",
#     description="Backend API for video selection and retrieval",
#     version="1.0.0",
#     docs_url="/docs",         # Swagger UI
#     redoc_url="/redoc",       # ReDoc documentation
#     openapi_url="/openapi.json"
# )
# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],  
#     allow_headers=["*"],
# )

# @app.post("/get-video-id")
# def get_video_id(payload: VideoFilter, db: Session = Depends(get_db)):
#     print(payload.dict())  # helpful for debugging

#     # video = db.query(Video).filter_by(
#         avatar_id=payload.avatar_id,
#         language=payload.language,
#         video_type=payload.video_type,
#         disease=payload.disease
#     ).first()

#     if not video:
#         raise HTTPException(status_code=404, detail="Currently video is not available")

#     return {
#         "video_id": video.id,
#         "video_url": video.video_url
#     }
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List,Optional
from video_data import sample_videos  # import your hardcoded data

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
class VideoFilter(BaseModel):
    avatar_id: int
    language: str
    video_type: str
    disease: Optional[str]=None

 # Optional in case of Stimulation

@app.post("/get-video-id")
def get_video_id(payload: VideoFilter):
    print(payload.dict())  # helpful for debugging

    for video in sample_videos:
        if (
            video["avatar_id"] == payload.avatar_id and
            video["language"] == payload.language and
            video["video_type"] == payload.video_type and
            (
                payload.video_type == "Stimulation" or
                video["disease"] == payload.disease
            )
        ):
            return {
                "video_url": video["video_url"]
            }

    raise HTTPException(status_code=404, detail="Currently video is not available")

