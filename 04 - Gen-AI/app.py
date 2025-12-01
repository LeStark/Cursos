# NOTA:
# Este archivo debe ejecutarse desde la terminal con:
# streamlit run app.py

import streamlit as st
import boto3

# -----------------------------
# Configuración básica
# -----------------------------
REGION = "us-east-2"
MODEL_ID = "us.amazon.nova-lite-v1:0"

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# -----------------------------
# Interfaz Streamlit
# -----------------------------
st.title("Demo simple de IA Generativa con Amazon Bedrock")
st.write(
    "Este ejemplo muestra cómo enviar un prompt a un modelo generativo "
    "y mostrar la respuesta en una aplicación web sencilla."
)

# Entrada de texto del usuario
user_prompt = st.text_area(
    "Escribe una instrucción o pregunta para el modelo:",
    placeholder="Ej: Explica qué es la IA generativa en términos simples"
)

# Botón para ejecutar la generación
if st.button("Generar respuesta"):

    if not user_prompt.strip():
        st.warning("Por favor escribe un texto antes de continuar.")
    else:
        with st.spinner("Generando respuesta..."):
            response = bedrock.converse(
                modelId=MODEL_ID,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"text": user_prompt}
                        ]
                    }
                ]
            )

            output_text = response["output"]["message"]["content"][0]["text"]

        st.subheader("Respuesta del modelo")
        st.write(output_text)