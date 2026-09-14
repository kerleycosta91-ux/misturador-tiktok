import streamlit as st
import moviepy.editor as mp
import itertools
import random
import os
import zipfile

st.title("🎬 Super Misturador TikTok Shop (Áudio + ZIP)")
st.write("Envie seus trechos e baixe TODAS as combinações com áudio original em um único arquivo ZIP!")

ganchos = st.file_uploader("1. Vídeos de GANCHO", accept_multiple_files=True, type=["mp4", "mov"])
desenvolvimentos = st.file_uploader("2. Vídeos de DESENVOLVIMENTO", accept_multiple_files=True, type=["mp4", "mov"])
ctas = st.file_uploader("3. Vídeos de CTA", accept_multiple_files=True, type=["mp4", "mov"])

if ganchos and desenvolvimentos and ctas:
    total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
    st.info(f"📊 Foram detectados: {len(ganchos)} Ganchos | {len(desenvolvimentos)} Desenvolvimentos | {len(ctas)} CTAs.")
    st.success(f"🔥 **{total_possivel} vídeos únicos com áudio** serão gerados combinando seus arquivos!")

    if st.button("🚀 Gerar TODOS os Vídeos Possíveis"):
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

            for idx, comb in enumerate(todas_combinacoes):
                g, d, c = comb[0].name, comb[1].name, comb[2].name
                output_name = f"video_tiktok_comb_{idx+1}.mp4"
                
                # Carrega os clipes mantendo o áudio original
                clip1 = mp.VideoFileClip(g).resize(height=1920, width=1080)
                clip2 = mp.VideoFileClip(d).resize(height=1920, width=1080)
                clip3 = mp.VideoFileClip(c).resize(height=1920, width=1080)
                
                # Junta preservando perfeitamente o áudio de cada trecho
                final_clip = mp.concatenate_videoclips([clip1, clip2, clip3], method="compose")
                final_clip.write_videofile(output_name, fps=30, codec="libx264", audio_codec="aac")
                
                # Fecha os clipes para liberar espaço da memória
                clip1.close()
                clip2.close()
                clip3.close()
                final_clip.close()
                
                lista_videos_gerados.append(output_name)
                
                progresso_atual = int(((idx + 1) / total_possivel) * 100)
                barra_progresso.progress(progresso_atual, text=f"🎬 Gerando Vídeos... {progresso_atual}% concluído ({idx+1}/{total_possivel})")

            barra_progresso.progress(100, text="📦 Compactando tudo em um arquivo ZIP...")
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for video_file in lista_videos_gerados:
                    if os.path.exists(video_file):
                        zipf.write(video_file)
                        os.remove(video_file) # Limpa o espaço

            st.success("🎉 Sensacional! Todas as variações com som foram geradas e compactadas.")
            
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
