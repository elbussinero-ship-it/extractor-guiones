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


# -----------------------
# EXTRACTOR
# -----------------------

st.header("📄 Extraer Transcripción")

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

        st.success("✅ Transcripción obtenida")

        st.text_area(
            "Resultado",
            texto,
            height=300
        )

    except Exception as e:

        st.error(str(e))


# -----------------------
# GENERADOR DE GANCHOS
# -----------------------

st.divider()

st.header("🔥 Generador de Ganchos Virales")

tema = st.text_input(
    "Escribe un tema",
    placeholder="Ejemplo: ajo"
)

if st.button("Generar Ganchos"):

    if tema:

        ganchos = [

            f"Lo que no te han contado de {tema}.",

            f"Pocos conocen este dato sobre {tema}.",

            f"La mayoría desconoce esto de {tema}.",

            f"Existe un detalle sobre {tema} que casi nadie menciona.",

            f"Lo que descubrí investigando sobre {tema}.",

            f"Muchos creen esto sobre {tema}.",

            f"¿Sabías esto sobre {tema}?",

            f"El error que muchas personas cometen con {tema}.",

            f"3 cosas que quizás no sabías sobre {tema}.",

            f"¿Es cierto todo lo que dicen sobre {tema}?",

            f"Lo que algunas personas desconocen sobre {tema}.",

            f"Hay algo sobre {tema} que podría sorprenderte.",

            f"Este dato sobre {tema} está llamando la atención.",

            f"¿Por qué tantas personas hablan de {tema}?",

            f"Un detalle curioso sobre {tema} que pocos conocen."

        ]

        st.success("✅ Ganchos generados")

        for i, gancho in enumerate(ganchos, start=1):

            st.write(f"{i}. {gancho}")

    else:

        st.warning("Escribe un tema.")
