import librosa
import numpy as np
import soundfile as sf
from io import BytesIO

def preprocess_audio(audio_bytes):
    """
    Preprocesa el audio para mejorar la transcripción en español.
    
    Args:
        audio_bytes: Bytes del archivo de audio
        
    Returns:
        Bytes del audio preprocesado
    """
    # Cargar audio
    y, sr = librosa.load(BytesIO(audio_bytes), sr=16000)
    
    # Normalización de volumen
    y = librosa.util.normalize(y)
    
    # Reducción de ruido (opcional)
    # y = nr.reduce_noise(y=y, sr=sr)
    
    # Convertir a bytes
    output = BytesIO()
    sf.write(output, y, sr, format='WAV')
    output.seek(0)
    
    return output