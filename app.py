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


# ==================================
# EXTRACTOR DE TRANSCRIPCIONES
# ==================================

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


# ==================================
# GENERADOR DE GANCHOS
# ==================================

st.divider()

st.header("🔥 Biblioteca de Ganchos Virales")

tema = st.text_input(
    "Escribe un tema",
    placeholder="Ejemplo: ajo"
)

if st.button("Generar Ganchos"):

    if tema:

        st.success("✅ Ganchos generados")

        # CURIOSIDAD

        st.subheader("🧠 Curiosidad")

        curiosidad = [

            f"Lo que no te han contado de {tema}.",

            f"Pocos conocen este dato sobre {tema}.",

            f"La mayoría desconoce esto de {tema}.",

            f"Existe un detalle sobre {tema} que casi nadie menciona.",

            f"Lo que descubrí investigando sobre {tema}."
        ]

        for i, gancho in enumerate(curiosidad, 1):

            st.write(f"{i}. {gancho}")

        # ERRORES

        st.subheader("⚠️ Error común")

        errores = [

            f"El error que muchas personas cometen con {tema}.",

            f"Algo que algunas personas hacen mal con {tema}.",

            f"Muchos pasan por alto este detalle sobre {tema}.",

            f"Un hábito relacionado con {tema} que suele generar dudas."
        ]

        for i, gancho in enumerate(errores, 1):

            st.write(f"{i}. {gancho}")

        # PREGUNTAS

        st.subheader("❓ Preguntas")

        preguntas = [

            f"¿Sabías esto sobre {tema}?",

            f"¿Es cierto todo lo que dicen sobre {tema}?",

            f"¿Habías escuchado esto sobre {tema}?",

            f"¿Por qué tantas personas hablan de {tema}?"
        ]

        for i, gancho in enumerate(preguntas, 1):

            st.write(f"{i}. {gancho}")

        # LISTAS

        st.subheader("📋 Listas")

        listas = [

            f"3 cosas que quizás no sabías sobre {tema}.",

            f"5 datos interesantes sobre {tema}.",

            f"4 detalles poco conocidos sobre {tema}.",

            f"3 razones por las que {tema} llama la atención."
        ]

        for i, gancho in enumerate(listas, 1):

            st.write(f"{i}. {gancho}")

        # MITOS

        st.subheader("🔍 Mitos")

        mitos = [

            f"Muchos creen esto sobre {tema}.",

            f"Existe una idea muy extendida sobre {tema}.",

            f"No todo lo que se dice sobre {tema} es correcto.",

            f"Un mito frecuente relacionado con {tema}."
        ]

        for i, gancho in enumerate(mitos, 1):

            st.write(f"{i}. {gancho}")

    else:

        st.warning("Escribe un tema.")
