import streamlit as st
import itertools
import random
import os
import zipfile
import subprocess

# Configuração visual premium para os seus clientes
st.set_page_config(page_title="ViraViral Pro - Criativos em Massa", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0F111A; color: #E2E8F0; }
    h1 { color: #FFFFFF !important; font-weight: 800 !important; background: linear-gradient(45deg, #FE2C55, #25F4EE); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    div.stButton > button:first-child { background: linear-gradient(135deg, #FE2C55 0%, #FF5A79 100%) !important; color: white !important; font-weight: bold !important; border-radius: 8px !important; border: none !important; width: 100%; height: 50px; box-shadow: 0 4px 15px rgba(254, 44, 85, 0.4) !important; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ ViraViral Pro")
st.subheader("Gerador Industrial de Vídeos com Som para o TikTok Shop")

# --- SEU SISTEMA DE SENHA PARA VENDAS ---
SENHA_CORRETA = "VIRAVIRAL77" 

st.sidebar.markdown("### 🔑 Ativação do Sistema")
senha_usuario = st.sidebar.text_input("Insira sua Chave de Acesso Paga:", type="password")

if senha_usuario != SENHA_CORRETA:
    st.warning("🔒 Área Restrita para Assinantes. Insira sua chave de acesso na barra lateral para liberar o misturador.")
    st.info("💡 **Como obter uma chave?** Faça o pagamento do seu acesso e receba sua chave de liberação instantaneamente.")
else:
    st.sidebar.success("✅ Acesso Premium Ativado!")
    
    # Layout de Uploads Organizado e Bonito
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🧲 1. Ganchos")
        ganchos = st.file_uploader("Arraste os ganchos (MP4)", accept_multiple_files=True, type=["mp4"])
    with col2:
        st.markdown("### 📦 2. Desenvolvimento")
        desenvolvimentos = st.file_uploader("Arraste o conteúdo (MP4)", accept_multiple_files=True, type=["mp4"])
    with col3:
        st.markdown("### 🛒 3. CTAs")
        ctas = st.file_uploader("Arraste as CTAs (MP4)", accept_multiple_files=True, type=["mp4"])

    st.markdown("---")

    if ganchos and desenvolvimentos and ctas:
        total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
        st.info(f"📊 Análise do Lote: {len(ganchos)} Ganchos × {len(desenvolvimentos)} Desenvolvimentos × {len(ctas)} CTAs = {total_possivel} combinações únicas com som original.")
        
        # Função Ultra-Leve usando FFmpeg (Une áudio e vídeo gastando pouca memória)
        def mesclar_videos_ffmpeg(v1, v2, v3, out_path):
            # Cria um arquivo de texto temporário listando os vídeos que serão colados
            list_file_path = f"lista_{random.randint(1000,9999)}.txt"
            with open(list_file_path, "w") as f:
                f.write(f"file '{v1}'\n")
                f.write(f"file '{v2}'\n")
                f.write(f"file '{v3}'\n")
            
            # Comando FFmpeg nativo do sistema para juntar os vídeos sem re-codificar (Super Rápido!)
            comando = [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0", 
                "-i", list_file_path, "-c", "copy", out_path
            ]
            
            # Executa em segundo plano de forma invisível e muito leve
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Deleta o arquivo de lista temporário
            if os.path.exists(list_file_path):
                os.remove(list_file_path)

        if st.button("🚀 RENDERIZAR TODOS OS VÍDEOS EM MASSA"):
            barra_progresso = st.progress(0, text="🎬 Gerando Vídeos com Áudio... Por favor, aguarde.")
            
            try:
                # Salva os uploads fisicamente no servidor temporário
                for f in ganchos + desenvolvimentos + ctas:
                    with open(f.name, "wb") as temp_f:
                        temp_f.write(f.read())

                todas_combinacoes = list(itertools.product(ganchos, desenvolvimentos, ctas))
                random.shuffle(todas_combinacoes)

                zip_filename = "lote_criativos_tiktok.zip"
                lista_videos_gerados = []

                # Processa cada combinação gerando o arquivo final com som
                for idx, comb in enumerate(todas_combinacoes):
                    g, d, c = comb.name, comb.name, comb.name
                    output_name = f"video_renderizado_{idx+1}.mp4"
                    
                    mesclar_videos_ffmpeg(g, d, c, output_name)
                    lista_videos_gerados.append(output_name)
                    
                    progresso_atual = int(((idx + 1) / total_possivel) * 100)
                    barra_progresso.progress(progresso_atual, text=f"🎬 Gerando Vídeos... {progresso_atual}% concluído ({idx+1}/{total_possivel})")

                # Junta tudo no arquivo ZIP solicitado
                barra_progresso.progress(100, text="📦 Compactando lote em arquivo único...")
                with zipfile.ZipFile(zip_filename, 'w') as zipf:
                    for video_file in lista_videos_gerados:
                        if os.path.exists(video_file):
                            zipf.write(video_file)
                            os.remove(video_file) # Apaga para economizar espaço
                
                # Limpa os arquivos originais de upload do servidor para não travar nas próximas rodadas
                for f in ganchos + desenvolvimentos + ctas:
                    if os.path.exists(f.name):
                        os.remove(f.name)

                st.success("🎉 Sensacional! Seu lote de criativos COM ÁUDIO foi gerado com sucesso.")
                
                with open(zip_filename, "rb") as file:
                    st.download_button(
                        label="📥 DOWNLOAD DO LOTE COMPLETO (.ZIP)", 
                        data=file, 
                        file_name=zip_filename, 
                        mime="application/zip"
                    )
            except Exception as e:
                st.error(f"Erro ao processar mídias: {e}")
    else:
        st.info("💡 Insira seus arquivos de vídeo nas categorias acima para ativar os motores.")
