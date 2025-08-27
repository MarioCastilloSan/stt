import os

# Configuración de modelos
WHISPER_MODEL = "base"  # Opciones: tiny, base, small, medium, large
EXAM_GENERATION_MODEL = "distilgpt2"  # Modelo ligero para generación

# Configuración de idioma
LANGUAGE = "es"  # Español

# Configuración de archivos
MAX_AUDIO_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_AUDIO_FORMATS = ["wav", "mp3", "flac"]

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "src", "sttext", "models")