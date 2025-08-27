EXAM_GENERATION_PROMPT = """
Genera 3 preguntas de opción múltiple en español basadas en el siguiente texto. 
Cada pregunta debe tener 3 opciones (A, B, C) e indicar cuál es la correcta.
Formato de salida:
Pregunta 1: [Pregunta]? 
A) [Opción A]
B) [Opción B]
C) [Opción C]
Correcta: [Letra de la opción correcta]

Texto: {text}
"""