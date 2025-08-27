import os
from typing import BinaryIO
from config.settings import MAX_AUDIO_SIZE, ALLOWED_AUDIO_FORMATS

def validate_audio(file: BinaryIO) -> bool:
    """
    Valida un archivo de audio subido.
    
    Args:
        file: Objeto de archivo subido
        
    Returns:
        True si es válido, False si no
    """
    # Verificar tamaño
    if hasattr(file, 'size') and file.size > MAX_AUDIO_SIZE:
        return False
    
    # Verificar extensión
    file_extension = os.path.splitext(file.name)[1][1:].lower()
    if file_extension not in ALLOWED_AUDIO_FORMATS:
        return False
    
    return True

def get_file_extension(filename: str) -> str:
    """Obtiene la extensión de un archivo."""
    return os.path.splitext(filename)[1][1:].lower()