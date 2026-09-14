import streamlit as st
import itertools
import random
import os
import zipfile
import subprocess

# Configuração da página com a identidade da sua nova marca
st.set_page_config(page_title="Vibe Certa - Misturador Automático", page_icon="🎬", layout="wide")

# Estilização visual voltada a Neuromarketing e Vendas (Dark Mode + Neon)
st.markdown("""
    <style>
    .stApp { background-color: #0B0D17; color: #E2E8F0; }
    h1 { color: #FFFFFF !important; font-weight: 800 !important; background: linear-gradient(45deg, #00F2FE, #4FACFE); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    h3 { color: #00F2FE !important; }
    div.stButton > button:first-child { background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%) !important; color: #0B0D17 !important; font-weight: bold !important; font-size: 16px !important; border-radius: 8px !important; border: none !important; width: 100%; height: 50px; box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3) !important; transition: all 0.3s ease; }
    div.stButton > button:first-child:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 242, 254, 0.5) !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Vibe Certa")
st.subheader("Misturador de Vídeos Inteligente para o TikTok Shop")

# --- SUA CHAVE DE ACESSO EXCLUSIVA PARA VENDER ---
CHAVE_SEC_CORRETA = "VIRAVIRAL77" 

st.sidebar.markdown("### 🔑 Ativação da Licença")
senha_usuario = st.sidebar.text_input("Insira sua Chave de Acesso:", type="password")

if senha_usuario != CHAVE_SEC_CORRETA:
    st.warning("🔒 Área Restrita para Assinantes. Insira sua chave na barra lateral para liberar os motores da Vibe Certa.")
    st.info("💡 **Deseja adquirir o acesso?** Efetue o pagamento e receba sua chave exclusiva para começar a lucrar com vídeos automáticos.")
else:
    st.sidebar.success("✅ Licença Ativada com Sucesso!")
    
    # Layout de Uploads Premium
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🧲 1. Seção de Ganchos")
        st.caption("Vídeos iniciais de forte retenção.")
        ganchos = st.file_uploader("Arraste os ganchos aqui (MP4)", accept_multiple_files=True, type=["mp4"])
    with col2:
        st.markdown("### 📦 2. Desenvolvimento")
        st.caption("Demonstração e quebra de objeções.")
        desenvolvimentos = st.file_uploader("Arraste o conteúdo aqui (MP4)", accept_multiple_files=True, type=["mp4"])
    with col3:
        st.markdown("### 🛒 3. Chamadas (CTA)")
        st.caption("Vídeos empurrando para o carrinho.")
        ctas = st.file_uploader("Arraste as CTAs aqui (MP4)", accept_multiple_files=True, type=["mp4"])

    st.markdown("---")

    if ganchos and desenvolvimentos and ctas:
        # Cálculo exato do total de variações possíveis
        total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
        st.info(f"📊 **Análise Estatística:** {len(ganchos)} Ganchos × {len(desenvolvimentos)} Desenvolvimentos × {len(ctas)} CTAs = {total_possivel} combinações exclusivas com áudio.")
        
        # Motor FFmpeg ultra-leve e imune a travamentos de memória do servidor
        def misturar_lote_ffmpeg(v1, v2, v3, caminho_saida):
            nome_lista_txt = f"lista_vibe_{random.randint(1000,9999)}.txt"
            with open(nome_lista_txt, "w") as f:
                f.write(f"file '{v1}'\n")
                f.write(f"file '{v2}'\n")
                f.write(f"file '{v3}'\n")
            
            comando = [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0", 
                "-i", nome_lista_txt, "-c", "copy", caminho_saida
            ]
            
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(nome_lista_txt):
                os.remove(nome_lista_txt)

        if st.button("🚀 INICIAR COMBINAÇÃO DE VÍDEOS EM MASSA"):
            barra_progresso = st.progress(0, text="⚙️ Gerando vídeos... Não feche esta página.")
            
            try:
                # Armazena temporariamente os arquivos enviados pelos usuários
                for f in ganchos + desenvolvimentos + ctas:
                    with open(f.name, "wb") as temp_f:
                        temp_f.write(f.read())

                # Monta a estrutura correta de combinações puxando o nome real da mídia
                todas_combinacoes = list(itertools.product(ganchos, desenvolvimentos, ctas))
                random.shuffle(todas_combinacoes)

                nome_arquivo_zip = "lote_videos_vibecerta.zip"
                arquivos_processados = []

                # Loop de geração corrigido (Extraindo os dados sem o erro de tupla)
                for idx, combinacao in enumerate(todas_combinacoes):
                    arquivo_g = combinacao[0].name
                    arquivo_d = combinacao[1].name
                    arquivo_c = combinacao[2].name
                    
                    nome_video_final = f"video_vibecerta_{idx+1}.mp4"
                    
                    misturar_lote_ffmpeg(arquivo_g, arquivo_d, arquivo_c, nome_video_final)
                    arquivos_processados.append(nome_video_final)
                    
                    # Atualização cirúrgica da barra na tela
                    progresso_atual = int(((idx + 1) / total_possivel) * 100)
                    barra_progresso.progress(progresso_atual, text=f"🎬 Criando variações... {progresso_atual}% completo ({idx+1}/{total_possivel})")

                # Junta os vídeos criados dentro do pacote ZIP compactado
                barra_progresso.progress(100, text="📦 Reunindo e gerando arquivo ZIP final...")
                with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
                    for arquivo_de_video in arquivos_processados:
                        if os.path.exists(arquivo_de_video):
                            zipf.write(arquivo_de_video)
                            os.remove(arquivo_de_video) # Limpa o lixo interno para não acumular
                
                # Apaga os rascunhos de uploads para o site ficar sempre limpo e rápido
                for f in ganchos + desenvolvimentos + ctas:
                    if os.path.exists(f.name):
                        os.remove(f.name)

                st.success("🎉 Sensacional! Seu lote de criativos COM SOM foi concluído pela inteligência Vibe Certa.")
                
                with open(nome_arquivo_zip, "rb") as file:
                    st.download_button(
                        label="📥 BAIXAR LOTE COMPLETO DE VÍDEOS (.ZIP)", 
                        data=file, 
                        file_name=nome_arquivo_zip, 
                        mime="application/zip"
                    )
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado no processamento: {e}")
    else:
        st.info("💡 Carregue os seus trechos de vídeo nos blocos superiores para liberar o painel de produção.")
