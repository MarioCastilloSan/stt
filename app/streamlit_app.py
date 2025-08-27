import streamlit as st
import sys
import os

# Agregar el directorio raíz del proyecto al PATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.sttext.transcriber import Transcriber
from src.exam_generator.generator import ExamGenerator
from src.utils.file_handler import validate_audio, get_file_extension
from config.settings import LANGUAGE

# Configuración de la página
st.set_page_config(
    page_title="Speech-to-Text + Generador de Exámenes",
    page_icon="🎤",
    layout="centered"
)

# Título y descripción
st.title("🎤 Speech-to-Text + Generador de Exámenes")
st.markdown(f"""
    Sube un archivo de audio en español para transcribirlo a texto y generar preguntas de examen automáticamente.
    Formatos soportados: WAV, MP3, FLAC (máx. 10MB)
    Idioma: Español
""")

# Widget para subir archivo
uploaded_file = st.file_uploader(
    "Selecciona un archivo de audio en español",
    type=["wav", "mp3", "flac"],
    help="Sube un archivo de audio en formato WAV, MP3 o FLAC (máx. 10MB)"
)

if uploaded_file:
    # Validar archivo
    if not validate_audio(uploaded_file):
        st.error("❌ Archivo inválido. Verifica el formato y tamaño (máx. 10MB).")
    else:
        # Mostrar información del archivo
        file_ext = get_file_extension(uploaded_file.name)
        st.success(f"✅ Archivo válido: {uploaded_file.name} ({uploaded_file.size/1024/1024:.2f} MB)")
        
        # Sección de transcripción
        st.header("📝 Transcripción en Español")
        transcriber = Transcriber()
        
        with st.spinner("Transcribiendo audio a español..."):
            # Reiniciar el puntero del archivo
            uploaded_file.seek(0)
            text = transcriber.transcribe(uploaded_file)
        
        # Mostrar texto transcrito
        st.text_area("Texto transcrito en español:", text, height=200)
        
        # Botón de descarga del texto
        st.download_button(
            label="📥 Descargar texto",
            data=text,
            file_name=f"transcripcion_es_{uploaded_file.name.split('.')[0]}.txt",
            mime="text/plain"
        )
        
        # Sección de generación de examen
        st.header("📝 Generador de Exámenes en Español")
        
        if st.button("Generar examen en español", type="primary"):
            generator = ExamGenerator()
            
            with st.spinner("Generando preguntas en español..."):
                exam = generator.generate(text)
            
            # Mostrar examen generado
            st.text_area("Examen generado en español:", exam, height=300)
            
            # Botón de descarga del examen
            st.download_button(
                label="📥 Descargar examen",
                data=exam,
                file_name=f"examen_es_{uploaded_file.name.split('.')[0]}.txt",
                mime="text/plain"
            )
        
        # Mostrar fragmento de muestra
        st.subheader("📄 Fragmento de muestra")
        sample_text = text[:200] + "..." if len(text) > 200 else text
        st.info(sample_text)