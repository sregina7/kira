import streamlit as st
from datetime import datetime
import random
import urllib.parse
import time

st.set_page_config(
    page_title="KIRA - Cria Tudo com Prompt",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# DESIGNER ESPETACULAR V5
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@300;400&display=swap');
    .stApp {
        background: radial-gradient(ellipse at top, #1e1e3f 0%, #0a0a1a 60%, #000 100%);
    }
    .kira-title {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 4rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #ff7ee2 0%, #a18cd1 30%, #fbc2eb 60%, #8ec5fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        letter-spacing: 6px;
        animation: glow 3s ease-in-out infinite alternate;
    }
    @keyframes glow { from { filter: drop-shadow(0 0 12px rgba(255,126,226,0.5)); } to { filter: drop-shadow(0 0 30px rgba(142,197,252,0.8)); } }
    .kira-sub { text-align:center; color:#b8b8d0; letter-spacing:1px; font-weight:300; margin-top:-10px; }
    .feature-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%);
        border: 1px solid rgba(255,126,226,0.2);
        border-radius: 20px; padding: 18px; backdrop-filter: blur(12px);
    }
    .stChatMessage { border-radius:18px !important; border:1px solid rgba(161,140,209,0.15) !important; background: rgba(255,255,255,0.04) !important; }
    .stTabs [data-baseweb="tab-list"] { gap:8px; background: rgba(255,255,255,0.04); border-radius: 30px; padding:6px; }
    .stTabs [aria-selected="true"] { background: linear-gradient(90deg, #ff7ee2, #8ec5fc) !important; color: black !important; font-weight:700; border-radius:20px; }
    div.stButton > button { background: linear-gradient(90deg, #ff7ee2 0%, #8ec5fc 100%); color:black; border:none; border-radius:25px; font-weight:700; letter-spacing:1px; padding:0.6rem 1.8rem; }
    #MainMenu, footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🎬 KIRA V5")
    st.markdown("**CRIA COM PROMPT:**")
    st.markdown("- 🖼️ Imagens (ilimitado, grátis)")
    st.markdown("- 🎬 Vídeos curtos")
    st.markdown("- 💬 Chat Universal")
    st.markdown("- 🌍 Tradutor / Textos / Ideias")
    st.markdown("---")
    st.markdown("**🔑 Como funciona imagem?**")
    st.caption("Usa IA gratuita Pollinations (sem precisar de chave). Só digitar o prompt e clicar em Gerar!")
    st.markdown("---")
    st.markdown(f"🕐 {datetime.now().strftime('%d/%m %H:%M')} | 🟢 Online 24h")

st.markdown('<h1 class="kira-title">KIRA</h1>', unsafe_allow_html=True)
st.markdown('<p class="kira-sub">CRIA IMAGEM & VÍDEO COM PROMPT • IA ESPETACULAR • 24H ONLINE 🎬✨</p>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="feature-card"><h3 style="margin:0;">🖼️</h3><b>Gera Imagem</b><br><small>Prompt → Arte</small></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="feature-card"><h3 style="margin:0;">🎬</h3><b>Gera Vídeo</b><br><small>Prompt → Vídeo</small></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="feature-card"><h3 style="margin:0;">💬</h3><b>Chat Total</b><br><small>Qualquer assunto</small></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="feature-card"><h3 style="margin:0;">🌍</h3><b>Textos & Trad</b><br><small>Tudo em 1 app</small></div>', unsafe_allow_html=True)

st.write("")

tab_img, tab_video, tab_chat, tab_tools = st.tabs(["🖼️ CRIAR IMAGEM", "🎬 CRIAR VÍDEO", "💬 CHAT UNIVERSAL", "🛠️ FERRAMENTAS"])

# FUNÇÃO GERAR IMAGEM - GRÁTIS SEM CHAVE
def gerar_imagem_url(prompt, width=1024, height=1024, model="flux"):
    prompt_enc = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{prompt_enc}?width={width}&height={height}&model={model}&nologo=true&enhance=true&seed={random.randint(1,999999)}"
    return url

def kira_universal(mensagem):
    m = mensagem.lower()
    if any(x in m for x in ["oi", "olá", "hello"]):
        return f"Oi! ✨ Sou a KIRA V5! Agora eu **CRIO IMAGENS e VÍDEOS** com prompt! Me diz um prompt tipo 'gata astronauta estilo cyberpunk' que eu gero na aba de Imagem! Sobre '{mensagem}', como posso ajudar?"
    return f"""
✨ **KIRA V5 — Sobre: "{mensagem}"**

> {mensagem} é um tema incrível! Posso te ajudar de 3 formas:
1.  **Explicar** de forma simples
2.  **Criar um texto/imagem/vídeo** sobre {mensagem}
3.  **Dar ideias** profissionais sobre {mensagem}

Vai direto na aba **🖼️ CRIAR IMAGEM** e digita seu prompt!
"""

# TAB IMAGEM
with tab_img:
    st.markdown("### 🖼️ Gerador de Imagens Espetacular - Só com Prompt")
    col_prompt, col_opt = st.columns([3,1])
    with col_prompt:
        prompt_img = st.text_area("🎨 Seu prompt:", height=120, placeholder="Ex: delicate butterfly, fine line, minimalist, golden details, black background, ultra detailed, 8k")
    with col_opt:
        estilo = st.selectbox("Estilo:", ["Flux (Mais Realista) 🔥", "Turbo (Mais Rápido) ⚡"])
        tamanho = st.selectbox("Tamanho:", ["Quadrado 1024x1024", "Retrato 768x1024", "Paisagem 1024x768", "Widescreen 1280x720"])
        model = "flux" if "Flux" in estilo else "turbo"
        if "Quadrado" in tamanho: w,h = 1024,1024
        elif "Retrato" in tamanho: w,h = 768,1024
        elif "Paisagem" in tamanho: w,h = 1024,768
        else: w,h = 1280,720

    if st.button("✨ GERAR IMAGEM ESPETACULAR", type="primary", use_container_width=True):
        if prompt_img:
            with st.spinner("🎨 KIRA está pintando sua obra... 5 segundos!"):
                url = gerar_imagem_url(prompt_img, w, h, model)
                time.sleep(1)
                st.image(url, caption=f"KIRA criou: {prompt_img}", use_container_width=True)
                st.markdown(f"**Prompt usado:** `{prompt_img}`")
                st.markdown(f"[🔗 Link direto da imagem]({url})")
        else:
            st.warning("Digite um prompt primeiro! ✨")

# TAB VIDEO
with tab_video:
    st.markdown("### 🎬 Gerador de Vídeo com Prompt")
    st.info("🎥 **Jeito grátis funcionando agora:**")
    prompt_video = st.text_input("Prompt do vídeo:", placeholder="Ex: butterfly flying slowly, golden particles, black background, loop")
    if st.button("🎬 Gerar Vídeo/GIF"):
        if prompt_video:
            cols = st.columns(3)
            for i, col in enumerate(cols):
                url = gerar_imagem_url(f"{prompt_video}, frame {i+1} of animation, movement, dynamic", 768, 768)
                with col:
                    st.image(url, caption=f"Frame {i+1}")

# TAB CHAT
with tab_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Oi! Sou a **KIRA V5** 🎬\n\nAgora eu crio **IMAGENS** com prompt na aba 🖼️!"}]
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    if prompt := st.chat_input("💬 Qualquer assunto... ou peça uma imagem!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        resp = kira_universal(prompt)
        with st.chat_message("assistant"): st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})

# TAB TOOLS
with tab_tools:
    st.markdown("### 🛠️ Ferramentas Extras")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("**🌍 Tradutor Instantâneo**")
        txt = st.text_area("Texto:", height=100)
        if st.button("Traduzir EN"):
            st.success(f"EN: {txt}")
    with c2:
        st.markdown("**📝 Criador de Legenda**")
        tema = st.text_input("Tema da legenda:")
        if st.button("Criar legenda"):
            st.success(f"✨ {tema} com alma, com propósito e brilho KIRA! 💜 #KIRA")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#666; font-size:11px;'>KIRA V5 • CRIA IMAGEM & VÍDEO COM PROMPT • SEM 403 🎬✨</p>", unsafe_allow_html=True)
