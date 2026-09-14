import streamlit as st
import itertools
import random
import os
import zipfile
import moviepy.editor as mp
st.set_page_config(page_title="Vibe Certa - Combinação de Vídeos", page_icon="■", layout="wide")
if "logado" not in st.session_state:
st.session_state.logado = False
st.markdown("""
<style>
.stApp {
background-color: #080A11;
background-image:
radial-gradient(at 10% 10%, rgba(0, 242, 254, 0.05) 0px, transparent 50%),
radial-gradient(at 90% 90%, rgba(254, 44, 85, 0.05) 0px, transparent 50%);
color: #E2E8F0;
font-family: 'Inter', sans-serif;
}
.stApp::before {
content: "■ ■ ■ ■ ■ ■ ■";
position: fixed;
top: 15%;
left: 5%;
font-size: 32px;
opacity: 0.03;
letter-spacing: 50px;
word-spacing: 30px;
pointer-events: none;
line-height: 200px;
width: 90%;
}
.banner-container {
text-align: center;
padding: 40px 20px;
background: linear-gradient(135deg, rgba(11, 15, 26, 0.8) 0%, rgba(20, 26, 43, 0.8) 100%);
border-radius: 20px;
border: 1px solid rgba(0, 242, 254, 0.15);
box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
margin-bottom: 30px;
}
.banner-title {
font-size: 64px !important;
font-weight: 900 !important;
margin: 0;
letter-spacing: -1px;
background: linear-gradient(45deg, #00F2FE, #4FACFE, #FE2C55);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
text-shadow: 0 0 40px rgba(0, 242, 254, 0.3);
}
.banner-subtitle {
color: #A0AEC0 !important;
font-size: 20px;
margin-top: 10px;
font-weight: 400;
}
div.stButton > button {
border-radius: 8px !important;
border: none !important;
font-weight: bold !important;
transition: all 0.3s ease !important;
}
/* Botão verde de ação em massa (Neuromarketing) */
.render-btn button {
background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
color: white !important;
height: 55px;
font-size: 18px !important;
box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3) !important;
width: 100%;
}
.render-btn button:hover {
transform: translateY(-2px);
box-shadow: 0 6px 25px rgba(16, 185, 129, 0.5) !important;
}
/* Botão de Download verde claro (Neuromarketing) */
div[data-testid="stDownloadButton"] > button {
background: linear-gradient(135deg, #34D399 0%, #10B981 100%) !important;
color: #080A11 !important;
height: 55px;
font-size: 18px !important;
font-weight: 800 !important;
box-shadow: 0 4px 20px rgba(52, 211, 153, 0.4) !important;
width: 100%;
}
div[data-testid="stDownloadButton"] > button:hover {
transform: translateY(-2px);
box-shadow: 0 6px 25px rgba(52, 211, 153, 0.6) !important;
}
</style>
""", unsafe_allow_html=True)
SENHA_CORRETA = "VIRAVIRAL77"
if not st.session_state.logado:
st.markdown("""
<div class='banner-container'>
<div class='banner-title'>■ VIBE CERTA</div>
<div class='banner-subtitle'>Combinação Industrial Inteligente de Vídeos</div>
</div>
""", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
senha_usuario = st.text_input("Digite aqui a senha para poder acessar o combinador de vídeos:", type="password")
st.markdown("""
<style>
.login-btn button {
background: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%) !important;
color: #080A11 !important;
height: 50px;
width: 100%;
font-size: 18px !important;
box-shadow: 0 4px 15px rgba(0, 242, 254, 0.3) !important;
}
.login-btn button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 242, 254, 0.5) !importa
nt; }
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='login-btn'>", unsafe_allow_html=True)
if st.button("■ ENTRAR NO SISTEMA"):
if senha_usuario == SENHA_CORRETA:
st.session_state.logado = True
st.rerun()
else:
st.error("■ Chave incorreta! Verifique os dados ou fale com o suporte.")
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br><p style='text-align: center; color: #718096; font-size: 14px;'>Plataforma Comercial Protegida.
Direitos Reservados Vibe Certa.</p>", unsafe_allow_html=True)
else:
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center; padding: 20px; background: rg
ba(20, 26, 43, 0.5); border-radius: 12px; margin-bottom: 25px; border: 1px solid rgba(0, 242, 254, 0.1);'>
<div>
<h2 style='margin:0; background: linear-gradient(45deg, #00F2FE, #4FACFE); -webkit-background-clip: t
ext; -webkit-text-fill-color: transparent; font-weight:800;'>■ Vibe Certa | Combinação de Vídeos</h2>
<p style='margin:0; color:#A0AEC0; font-size:14px;'>Acesso Premium Ativo • Produção de Criativos TikT
ok & Kwai</p>
</div>
</div>
""", unsafe_allow_html=True)
col_out1, col_out2 = st.columns(2)
with col_out2:
st.markdown("""
<style>
.sair-btn button {
background: #1A202C !important;
color: #E2E8F0 !important;
border: 1px solid #4A5568 !important;
width: 100%;
}
.sair-btn button:hover { background: #FE2C55 !important; color: white !important; border-color: #FE2C55 !
important; }
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='sair-btn'>", unsafe_allow_html=True)
if st.button("■ Sair do Site"):
st.session_state.logado = False
st.rerun()
st.markdown("</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
st.markdown("<h3 style='color:#00F2FE !important;'>■ 1. Seção de Ganchos</h3>", unsafe_allow_html=True)
ganchos = st.file_uploader("Arraste os ganchos aqui (MP4)", accept_multiple_files=True, type=["mp4"])
with col2:
st.markdown("<h3 style='color:#00F2FE !important;'>■ 2. Desenvolvimento</h3>", unsafe_allow_html=True)
desenvolvimentos = st.file_uploader("Arraste o conteúdo aqui (MP4)", accept_multiple_files=True, type=["mp4"]
)
with col3:
st.markdown("<h3 style='color:#00F2FE !important;'>■ 3. Chamadas (CTA)</h3>", unsafe_allow_html=True)
ctas = st.file_uploader("Arraste as CTAs aqui (MP4)", accept_multiple_files=True, type=["mp4"])
st.markdown("---")
if ganchos and desenvolvimentos and ctas:
total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
st.info(f"■ **Análise do Lote:** {total_possivel} combinações exclusivas com som original.")
st.markdown("<div class='render-btn'>", unsafe_allow_html=True)
executar_lote = st.button("■ INICIAR COMBINAÇÃO DE VÍDEOS EM MASSA")
st.markdown("</div>", unsafe_allow_html=True)
if executar_lote:
barra_progresso = st.progress(0, text="■■ Motores ativados... Processando áudio e vídeo.")
try:
for f in ganchos + desenvolvimentos + ctas:
with open(f.name, "wb") as temp_f:
temp_f.write(f.read())
todas_combinacoes = list(itertools.product(ganchos, desenvolvimentos, ctas))
random.shuffle(todas_combinacoes)
nome_arquivo_zip = "lote_videos_vibecerta.zip"
arquivos_processados = []
for idx, combinacao in enumerate(todas_combinacoes):
g_item, d_item, c_item = combinacao
clip1 = mp.VideoFileClip(g_item.name)
clip2 = mp.VideoFileClip(d_item.name)
clip3 = mp.VideoFileClip(c_item.name)
final_clip = mp.concatenate_videoclips([clip1, clip2, clip3], method="compose")
nome_video_final = f"video_vibecerta_{idx+1}.mp4"
final_clip.write_videofile(nome_video_final, fps=24, codec="libx264", audio_codec="aac", logger=N
one)
clip1.close()
clip2.close()
clip3.close()
final_clip.close()
arquivos_processados.append(nome_video_final)
progresso_atual = int(((idx + 1) / total_possivel) * 100)
barra_progresso.progress(progresso_atual, text=f"■ Criando variações... {idx+1}/{total_possivel}"
)
with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
for arquivo in arquivos_processados:
zipf.write(arquivo)
os.remove(arquivo)
for f in ganchos + desenvolvimentos + ctas:
if os.path.exists(f.name):
os.remove(f.name)
barra_progresso.empty()
st.success("■ Lote gerado com sucesso absoluto! Seus criativos de alta conversão estão prontos.")
with open(nome_arquivo_zip, "rb") as f_zip:
st.download_button(
label="■ BAIXAR PACOTE DE VÍDEOS (.ZIP)",
data=f_zip,
file_name=nome_arquivo_zip,
mime="application/zip"
)
except Exception as e:
st.error(f"■ Ocorreu um erro técnico na renderização: {e}")
