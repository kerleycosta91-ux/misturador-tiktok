import streamlit as st
import cv2
import numpy as np
import itertools
import random
import os

st.title("🎬 Super Misturador TikTok Shop (Modo Total)")
st.write("Envie seus trechos e o sistema gerará automaticamente TODAS as combinações possíveis!")

ganchos = st.file_uploader("1. Vídeos de GANCHO", accept_multiple_files=True, type=["mp4", "mov"])
desenvolvimentos = st.file_uploader("2. Vídeos de DESENVOLVIMENTO", accept_multiple_files=True, type=["mp4", "mov"])
ctas = st.file_uploader("3. Vídeos de CTA", accept_multiple_files=True, type=["mp4", "mov"])

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

# Se houver vídeos em todas as categorias, faz o cálculo automático
if ganchos and desenvolvimentos and ctas:
    total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
    st.info(f"📊 Foram detectados: {len(ganchos)} Ganchos | {len(desenvolvimentos)} Desenvolvimentos | {len(ctas)} CTAs.")
    st.success(f"🔥 **{total_possivel} vídeos únicos** serão gerados combinando todos os seus arquivos!")

    if st.button("🚀 Gerar TODOS os Vídeos Possíveis"):
        with st.spinner("Processando combinações... Aguarde até o final."):
            try:
                # Salva os uploads temporariamente
                for f in ganchos + desenvolvimentos + ctas:
                    with open(f.name, "wb") as temp_f:
                        temp_f.write(f.read())

                # Gera todas as combinações sem repetir nenhuma
                todas_combinacoes = list(itertools.product(ganchos, desenvolvimentos, ctas))
                
                # Embaralha a ordem de criação para não salvar em sequência óbvia
                random.shuffle(todas_combinacoes)

                for idx, comb in enumerate(todas_combinacoes):
                    g, d, c = comb[0].name, comb[1].name, comb[2].name
                    output_name = f"video_tiktok_comb_{idx+1}.mp4"
                    
                    mesclar_videos(g, d, c, output_name)
                    
                    with open(output_name, "rb") as file:
                        st.download_button(
                            label=f"📥 Baixar Vídeo {idx+1} de {total_possivel}", 
                            data=file, 
                            file_name=output_name, 
                            mime="video/mp4"
                        )
                st.success("🎉 Sensacional! Todas as variações foram geradas.")
            except Exception as e:
                st.error(f"Erro ao processar os arquivos: {e}")
else:
    st.warning("Aguardando o envio de arquivos em todas as 3 categorias para calcular o total.")
