import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re


st.title("🎬 Extractor de Guiones para Reels")


def obtener_video_id(entrada):

    entrada = entrada.strip()

    if len(entrada) == 11:
        return entrada

    match = re.search(r"shorts/([a-zA-Z0-9_-]+)", entrada)
    if match:
        return match.group(1)

    match = re.search(r"v=([a-zA-Z0-9_-]+)", entrada)
    if match:
        return match.group(1)

    return entrada


url = st.text_input(
    "Pega la URL o ID del video"
)

if st.button("Extraer Transcripción"):

    try:

        video_id = obtener_video_id(url)

        api = YouTubeTranscriptApi()

        transcript = api.fetch(
            video_id,
            languages=["es"]
        )

        texto = ""

        for item in transcript:
            texto += item.text + " "

        st.success("Transcripción obtenida")

        st.text_area(
            "Resultado",
            texto,
            height=300
        )

    except Exception as e:

        st.error(str(e))