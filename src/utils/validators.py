from pydantic import BaseModel, validator
from typing import Optional

class AudioFile(BaseModel):
    filename: str
    content_type: str
    size: int

    @validator('size')
    def check_size(cls, v):
        from config.settings import MAX_AUDIO_SIZE
        if v > MAX_AUDIO_SIZE:
            raise ValueError(f"El archivo excede el tamaño máximo de {MAX_AUDIO_SIZE/1024/1024}MB")
        return v

    @validator('filename')
    def check_extension(cls, v):
        from config.settings import ALLOWED_AUDIO_FORMATS
        ext = v.split('.')[-1].lower()
        if ext not in ALLOWED_AUDIO_FORMATS:
            raise ValueError(f"Extensión no permitida. Use: {', '.join(ALLOWED_AUDIO_FORMATS)}")
        return v