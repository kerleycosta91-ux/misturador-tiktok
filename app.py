import streamlit as st
import cv2
import numpy as np
import itertools
import random
import os
import zipfile

st.title("🎬 Super Misturador TikTok Shop (Modo ZIP)")
st.write("Envie seus trechos e baixe TODAS as combinações possíveis em um único arquivo compactado!")

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

if ganchos and desenvolvimentos and ctas:
    total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
    st.info(f"📊 Foram detectados: {len(ganchos)} Ganchos | {len(desenvolvimentos)} Desenvolvimentos | {len(ctas)} CTAs.")
    st.success(f"🔥 **{total_possivel} vídeos únicos** serão gerados combinando todos os seus arquivos!")

    if st.button("🚀 Gerar TODOS os Vídeos Possíveis"):
        # Criando a barra de progresso solicitada
        barra_progresso = st.progress(0, text="🎬 Gerando Vídeos... Aguarde")
        
        try:
            # Salva os uploads temporariamente
            for f in ganchos + desenvolvimentos + ctas:
                with open(f.name, "wb") as temp_f:
                    temp_f.write(f.read())

            todas_combinacoes = list(itertools.product(ganchos, desenvolvimentos, ctas))
            random.shuffle(todas_combinacoes)

            zip_filename = "todos_os_videos_tiktok.zip"
            lista_videos_gerados = []

            # Loop de geração dos vídeos
            for idx, comb in enumerate(todas_combinacoes):
                g, d, c = comb[0].name, comb[1].name, comb[2].name
                output_name = f"video_tiktok_comb_{idx+1}.mp4"
                
                # Executa a junção dos trechos
                mesclar_videos(g, d, c, output_name)
                lista_videos_gerados.append(output_name)
                
                # Atualiza dinamicamente a barrinha com a porcentagem concluída
                progresso_atual = int(((idx + 1) / total_possivel) * 100)
                barra_progresso.progress(progresso_atual, text=f"🎬 Gerando Vídeos... {progresso_atual}% concluído ({idx+1}/{total_possivel})")

            # Finalizou a criação: junta tudo dentro do arquivo ZIP solicitado
            barra_progresso.progress(100, text="📦 Compactando tudo em um arquivo ZIP...")
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for video_file in lista_videos_gerados:
                    if os.path.exists(video_file):
                        zipf.write(video_file)
                        os.remove(video_file) # Remove o vídeo solto para não acumular lixo no servidor

            st.success("🎉 Sensacional! Todas as variações foram geradas e zipadas com sucesso.")
            
            # Mostra o botão único de Download contendo o arquivo ZIP completo
            with open(zip_filename, "rb") as file:
                st.download_button(
                    label="📥 Download (Baixar todos os vídeos de uma vez)", 
                    data=file, 
                    file_name=zip_filename, 
                    mime="application/zip"
                )
        except Exception as e:
            st.error(f"Erro ao processar os arquivos: {e}")
else:
    st.warning("Aguardando o envio de arquivos em todas as 3 categorias para calcular o total.")
