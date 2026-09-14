import streamlit as st
import cv2
import numpy as np
import random
import os

st.title("🎬 Misturador de Vídeos - TikTok Shop")
st.write("Envie seus trechos para gerar vídeos únicos com transições!")

ganchos = st.file_uploader("1. Vídeos de GANCHO", accept_multiple_files=True, type=["mp4", "mov"])
desenvolvimentos = st.file_uploader("2. Vídeos de DESENVOLVIMENTO", accept_multiple_files=True, type=["mp4", "mov"])
ctas = st.file_uploader("3. Vídeos de CTA", accept_multiple_files=True, type=["mp4", "mov"])

qtd = st.number_input("Quantas variações quer gerar?", min_value=1, max_value=20, value=3)

def mesclar_videos(v1, v2, v3, out_path):
    cap1 = cv2.VideoCapture(v1)
    cap2 = cv2.VideoCapture(v2)
    cap3 = cv2.VideoCapture(v3)
    
    width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap1.get(cv2.CAP_PROP_FPS)) or 30
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))
    
    for cap in [cap1, cap2, cap3]:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
        cap.release()
    out.release()

if st.button("🚀 Gerar e Misturar Vídeos"):
    if not ganchos or not desenvolvimentos or not ctas:
        st.error("Por favor, envie pelo menos 1 vídeo em cada categoria!")
    else:
        with st.spinner("Misturando vídeos... Aguarde."):
            try:
                for f in ganchos + desenvolvimentos + ctas:
                    with open(f.name, "wb") as temp_f:
                        temp_f.write(f.read())

                for v_idx in range(int(qtd)):
                    g = random.choice(ganchos).name
                    d = random.choice(desenvolvimentos).name
                    c = random.choice(ctas).name
                    
                    output_name = f"video_tiktok_{v_idx+1}.mp4"
                    mesclar_videos(g, d, c, output_name)
                    
                    with open(output_name, "rb") as file:
                        st.download_button(label=f"📥 Baixar Vídeo {v_idx+1}", data=file, file_name=output_name, mime="video/mp4")
                st.success("Todos os vídeos foram gerados com sucesso!")
            except Exception as e:
                st.error(f"Erro ao processar: {e}")
