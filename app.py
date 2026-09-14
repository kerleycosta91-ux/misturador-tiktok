import streamlit as st
import moviepy.editor as mp
import random
import os

st.title("🎬 Misturador de Vídeos - TikTok Shop")
st.write("Envie seus trechos para gerar vídeos únicos com transições!")

ganchos = st.file_uploader("1. Vídeos de GANCHO", accept_multiple_files=True, type=["mp4", "mov"])
desenvolvimentos = st.file_uploader("2. Vídeos de DESENVOLVIMENTO", accept_multiple_files=True, type=["mp4", "mov"])
ctas = st.file_uploader("3. Vídeos de CTA", accept_multiple_files=True, type=["mp4", "mov"])

qtd = st.number_input("Quantas variações quer gerar?", min_value=1, max_value=20, value=3)

if st.button("🚀 Gerar e Misturar Vídeos"):
    if not ganchos or not desenvolvimentos or not ctas:
        st.error("Por favor, envie pelo menos 1 vídeo em cada categoria!")
    else:
        with st.spinner("Misturando e aplicando transições... Aguarde."):
            try:
                # Salvar arquivos temporários
                for i, list_files in enumerate([ganchos, desenvolvimentos, ctas]):
                    for f in list_files:
                        with open(f.name, "wb") as temp_f:
                            temp_f.write(f.read())

                for v_idx in range(int(qtd)):
                    g_escolhido = random.choice(ganchos).name
                    d_escolhido = random.choice(desenvolvimentos).name
                    c_escolhido = random.choice(ctas).name

                    clip1 = mp.VideoFileClip(g_escolhido).resize(height=1920, width=1080)
                    clip2 = mp.VideoFileClip(d_escolhido).resize(height=1920, width=1080)
                    clip3 = mp.VideoFileClip(c_escolhido).resize(height=1920, width=1080)

                    # Mistura com efeito Crossfade (transição suave de 0.5 segundos)
                    final_clip = mp.concatenate_videoclips([clip1, clip2, clip3], method="compose", padding=-0.5)
                    
                    output_name = f"video_tiktok_{v_idx+1}.mp4"
                    final_clip.write_videofile(output_name, fps=30, codec="libx264", audio_codec="aac")
                    
                    clip1.close()
                    clip2.close()
                    clip3.close()

                    with open(output_name, "rb") as file:
                        st.download_button(label=f"📥 Baixar Vídeo {v_idx+1}", data=file, file_name=output_name, mime="video/mp4")
                st.success("Todos os vídeos foram gerados com sucesso!")
            except Exception as e:
                st.error(f"Erro ao processar: {e}")
