# NOTA:
# Este archivo debe ejecutarse desde la terminal con:
# streamlit run app.py

import streamlit as st
import boto3
import json
import base64

# -----------------------------
# Configuración básica
# -----------------------------
REGION = "us-east-2"
# Cambiamos al Model ID para generación de imágenes de Amazon Titan
MODEL_ID = "us.amazon.titan-image-generator-v1" 

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# -----------------------------
# Interfaz Streamlit
# -----------------------------
st.title("Demo de Generación de Imágenes con Amazon Bedrock")
st.write(
    "Introduce un prompt para generar una imagen utilizando el modelo Titan Image Generator."
)

# Entrada de texto del usuario (para el prompt de imagen)
user_prompt = st.text_area(
    "Describe la imagen que quieres generar:",
    placeholder="Ej: Un astronauta montando a caballo en un estilo de arte digital fotorrealista 4K."
)

# Botón para ejecutar la generación
if st.button("Generar Imagen"):

    if not user_prompt.strip():
        st.warning("Por favor escribe un prompt antes de continuar.")
    else:
        with st.spinner("Generando imagen..."):
            # 1. Preparar el payload para invoke_model
            # Los modelos de imagen esperan un JSON específico como entrada.
            body = json.dumps({
                "textToImageParams": {
                    "text": user_prompt
                },
                "taskType": "TEXT_IMAGE",
                "imageGenerationConfig": {
                    "numberOfImages": 1,
                    "quality": "standard",
                    "cfgScale": 8.0,
                    "seed": 0,
                    "width": 512,
                    "height": 512
                }
            })

            # 2. Invocar el modelo usando invoke_model
            response = bedrock_runtime.invoke_model(
                body=body,
                modelId=MODEL_ID,
                contentType='application/json',
                accept='application/json'
            )

            # 3. Procesar la respuesta
            response_body = json.loads(response.get('body').read())
            
            # La imagen generada viene en base64 dentro de una lista 'images'
            base64_image_bytes = response_body["images"][0].encode('utf-8')
            
            # Decodificar la imagen de base64 a bytes binarios para Streamlit
            image_bytes = base64.b64decode(base64_image_bytes)

        st.subheader("Imagen Generada")
        # Mostrar la imagen en la interfaz de Streamlit
        st.image(image_bytes, caption="Imagen generada por IA", use_column_width=True)