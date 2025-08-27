import whisper
import os
import tempfile
from typing import Optional
from config.settings import WHISPER_MODEL
from src.utils.audio_processor import preprocess_audio

class Transcriber:
    def __init__(self, model_name: Optional[str] = None):
        self.model_name = model_name or WHISPER_MODEL
        self.model = whisper.load_model(self.model_name)
            
    def transcribe(self, audio_file) -> str:
        if hasattr(audio_file, 'read'):
            # Preprocesar el audio
            processed_audio = preprocess_audio(audio_file.read())
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(processed_audio.read())
                tmp_path = tmp.name
            
            result = self.model.transcribe(
                tmp_path,
                language="es",
                fp16=False,
                temperature=0.0
            )
            
            os.unlink(tmp_path)
        else:
            result = self.model.transcribe(
                audio_file,
                language="es",
                fp16=False,
                temperature=0.0
            )
            
        return result["text"]