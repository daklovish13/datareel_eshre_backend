from pydantic import BaseModel

class VideoFilter(BaseModel):
    avatar_id: int
    language: str
    video_type: str
    disease: str



