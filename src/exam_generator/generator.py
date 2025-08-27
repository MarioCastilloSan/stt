from transformers import pipeline
from .prompts import EXAM_GENERATION_PROMPT
from config.settings import EXAM_GENERATION_MODEL, LANGUAGE

class ExamGenerator:
    def __init__(self):
        """Inicializa el modelo de generación de texto."""
        self.generator = pipeline(
            'text-generation', 
            model=EXAM_GENERATION_MODEL,
            max_length=500
        )

    def generate(self, text: str) -> str:
        """
        Genera preguntas de examen basadas en un texto.
        
        Args:
            text: Texto de entrada para generar preguntas
            
        Returns:
            Texto con preguntas generadas
        """
        # Asegurarnos de que el texto esté en español
        if LANGUAGE == "es":
            prompt = EXAM_GENERATION_PROMPT.format(text=text)
            result = self.generator(prompt, num_return_sequences=1)
            return result[0]['generated_text']
        else:
            raise ValueError("Solo se soporta español en esta versión")