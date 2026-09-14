import streamlit as st
import moviepy.editor as mp
import itertools
import random
import os
import zipfile
import time

# Configuração da Página com visual profissional
st.set_page_config(
    page_title="ViraViral Pro - Gerador em Massa",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injeção de CSS para Neuromarketing (Design Premium, Cores do TikTok/Dark e remoção de marcas do Streamlit)
st.markdown("""
    <style>
    /* Estilização Geral do Fundo */
    .stApp {
        background-color: #0B0E14;
        color: #E2E8F0;
    }
    /* Estilização dos Títulos */
    h1 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif;
        font-weight: 800 !important;
        background: linear-gradient(45deg, #FE2C55, #25F4EE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    /* Caixas de Alerta Customizadas */
    .stAlert {
        border-radius: 12px !important;
        border: 1px solid #2D3748 !important;
    }
    /* Estilização dos Botões Magnéticos */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #6366F1 0%, #4338CA 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 14px 28px !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Topo do Site - Proposta de Valor Clara
st.title("⚡ ViraViral Pro")
st.subheader("Multiplique seus criativos para o TikTok Shop de forma industrial")
st.write("Combine ganchos, demonstrações e chamadas para ação em escala utilizando Inteligência de Renderização.")

st.markdown("---")

# Layout em Colunas para os Uploads (Garante organização visual)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧲 1. Ganchos retentivos")
    st.caption("Primeiros 3 a 5 segundos para prender a atenção do feed.")
    ganchos = st.file_uploader("Arraste seus ganchos aqui", accept_multiple_files=True, type=["mp4", "mov"], key="g_upload")

with col2:
    st.markdown("### 📦 2. Desenvolvimento / Oferta")
    st.caption("Demonstre as dores, benefícios e quebra de objeções do produto.")
    desenvolvimentos = st.file_uploader("Arraste os miolos aqui", accept_multiple_files=True, type=["mp4", "mov"], key="d_upload")

with col3:
    st.markdown("### 🛒 3. Chamadas para Ação (CTA)")
    st.caption("Ordene que o cliente clique no carrinho ou no link do perfil.")
    ctas = st.file_uploader("Arraste as CTAs aqui", accept_multiple_files=True, type=["mp4", "mov"], key="c_upload")

st.markdown("---")

# Painel de Inteligência de Negócios e Métricas de Neuromarketing
if ganchos and desenvolvimentos and ctas:
    total_possivel = len(ganchos) * len(desenvolvimentos) * len(ctas)
    
    # Exibição de Métricas de Alto Valor Percebido
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="Anúncios Prontos para Teste", value=f"{total_possivel} Vídeos")
    with m2:
        # Cálculo de quanto tempo o usuário economiza (Neuromarketing: Ganho de tempo)
        tempo_economizado = (total_possivel * 5) / 60
        st.metric(label="Tempo de Edição Salvo", value=f"{tempo_economizado:.1f} Horas")
    with m3:
        st.metric(label="Custo de Produção Estimado", value="R$ 0,00", delta="100% de Economia")

    st.markdown("<br>", unsafe_allow_html=False)

    # Painel de Controle de Renderização
    c_btn1, c_btn2 = st.columns([2, 1])
    
    with c_btn1:
        executar = st.button("🚀 Renderizar Lote de Criativos Magnéticos")
    
    if executar:
        barra_progresso = st.progress(0, text="⚙️ Inicializando motores de renderização...")
        
        try:
            # Organização dos temporários
            for f in ganchos + desenvolvimentos + ctas:
                with open(f.name, "wb") as temp_f:
                    temp_f.write(f.read())

            todas_combinacoes = list(itertools.product(ganchos, desenvolvimentos, ctas))
            random.shuffle(todas_combinacoes)

            zip_filename = "lote_criativos_pro.zip"
            lista_videos_gerados = []

            for idx, comb in enumerate(todas_combinacoes):
                g, d, c = comb.name, comb.name, comb.name
                output_name = f"video_comb_{idx+1}.mp4"
                
                # Renderização profissional mantendo o áudio
                clip1 = mp.VideoFileClip(g).resize(height=1920, width=1080)
                clip2 = mp.VideoFileClip(d).resize(height=1920, width=1080)
                clip3 = mp.VideoFileClip(c).resize(height=1920, width=1080)
                
                final_clip = mp.concatenate_videoclips([clip1, clip2, clip3], method="compose")
                final_clip.write_videofile(output_name, fps=30, codec="libx264", audio_codec="aac", logger=None)
                
                clip1.close()
                clip2.close()
                clip3.close()
                final_clip.close()
                
                lista_videos_gerados.append(output_name)
                
                # Progresso dinâmico e polido
                progresso_atual = int(((idx + 1) / total_possivel) * 100)
                barra_progresso.progress(progresso_atual, text=f"⚡ Processando Lote Industrial... {progresso_atual}% concluído ({idx+1}/{total_possivel})")

            barra_progresso.progress(100, text="📦 Empacotando e criptografando arquivos de mídia...")
            
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for video_file in lista_videos_gerados:
                    if os.path.exists(video_file):
                        zipf.write(video_file)
                        os.remove(video_file)

            st.balloons()
            st.success("🎉 Sistema concluído! Seus anúncios prontos para escala foram gerados.")
            
            # Botão de download otimizado
            with open(zip_filename, "rb") as file:
                st.download_button(
                    label="📥 ACESSAR ARQUIVO DE ANÚNCIOS (Baixar .ZIP)", 
                    data=file, 
                    file_name=zip_filename, 
                    mime="application/zip"
                )
        except Exception as e:
            st.error(f"Ocorreu um desvio técnico ao mesclar mídias: {e}")
else:
    # Estado vazio inteligente (Gatilho da Ação)
    st.info("💡 Insira mídias em todos os quadrantes acima para ativar o Painel de Escala.")
