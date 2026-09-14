import streamlit as st
import os, urllib.parse, random, time
from datetime import datetime

st.set_page_config(page_title="KIRA V15 - Preto e Dourado", page_icon="💛", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&family=Playfair+Display:wght@700&display=swap');
.stApp { background: radial-gradient(ellipse at top, #1a1508 0%, #000000 65%) !important; background-color: #000000 !important;}
.kira-title { font-family:'Playfair Display', serif; font-size: clamp(2.4rem,8vw,4.2rem); font-weight:800; text-align:center; background: linear-gradient(90deg,#FFD700,#FFC300,#FFAA00,#FFD700); -webkit-background-clip:text; -webkit-text-fill-color:transparent; letter-spacing:6px;}
.kira-sub { text-align:center; color:#C9A86A; font-size:0.85rem; letter-spacing:4px; margin-top:-8px; font-family:'Space Grotesk',sans-serif;}
.stChatMessage { border-radius:18px !important; background: rgba(20,18,8,0.8) !important; border:1px solid rgba(255,215,0,0.25) !important; }
div.stButton > button { background: linear-gradient(90deg,#FFD700,#FFAA00) !important; color:#000 !important; border-radius:24px; font-weight:900; height:52px; font-size:16px; border:1px solid #FFD700 !important; box-shadow: 0 0 15px rgba(255,215,0,0.4);}
section[data-testid="stSidebar"] { background: linear-gradient(180deg, #0a0a0a 0%, #1a1508 100%) !important; border-right: 1px solid rgba(255,215,0,0.2) !important;}
#MainMenu, footer, header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

def gerar_url_fiel(prompt,w=1024,h=1024):
    final = f"{prompt.strip()}, ultra detailed, sharp focus, high quality, black and gold luxurious style, golden cinematic lighting, safe for work"
    enc = urllib.parse.quote(final)
    seed = random.randint(1,999999999)
    return f"https://image.pollinations.ai/prompt/{enc}?width={w}&height={h}&model=flux&seed={seed}&nologo=true&enhance=true"

# --- LOGO CORRIGIDA - ACEITA geometric_lioness_k_icon.jpg ---
with st.sidebar:
    logo_candidatos = [
        "logo.png","logo.jpg","logo.jpeg",
        "geometric_lioness_k_icon.jpg",  # <-- SUA LOGO ATUAL
        "geometric_lioness_k_icon.png",
        "kira.png","kira.jpg"
    ]
    logo_achada = None
    for nome in logo_candidatos:
        if os.path.exists(nome):
            logo_achada = nome
            break
    
    if logo_achada:
        st.image(logo_achada, width=160)
        st.markdown("<p style='text-align:center; color:#FFD700; font-size:12px; letter-spacing:2px;'>KIRA V15</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align:center; color:#FFD700;'>KIRA V15</h2>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**💛 PRETO & DOURADO**")
    st.caption(f"Logo: {logo_achada if logo_achada else 'não achada'}")
    tam = st.selectbox("Tamanho imagem:", ["Quadrado 1024x1024","Retrato 768x1024","Paisagem 1024x768","Story 720x1280"])
    st.session_state["tam"]=tam

st.markdown('<h1 class="kira-title">KIRA</h1>', unsafe_allow_html=True)
st.markdown('<p class="kira-sub">V15 • PRETO E DOURADO • LUXO • INDEPENDENTE</p>', unsafe_allow_html=True)

tab_img, tab_chat = st.tabs(["🖼️ IMAGEM","💬 CHAT"])

with tab_img:
    prompt = st.text_area("Seu prompt:", height=110, placeholder="Ex: borboletas douradas descendo no nariz de dragão preto")
    if st.button("✨ GERAR EM PRETO E DOURADO", type="primary", use_container_width=True):
        if prompt and len(prompt.strip())>2:
            t = st.session_state.get("tam","Quadrado 1024x1024")
            w,h = (1024,1024) if "Quadrado" in t else (768,1024) if "Retrato" in t else (1024,768) if "Paisagem" in t else (720,1280)
            url = gerar_url_fiel(prompt,w,h)
            st.image(url, caption=prompt, use_container_width=True)
            st.markdown(f"[⬇️ Baixar]({url})")

with tab_chat:
    if "msgs" not in st.session_state:
        st.session_state.msgs=[{"role":"assistant","content":"KIRA V15 preto e dourado ativa 🖤💛 Logo corrigida!"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p:=st.chat_input("Fala..."):
        st.session_state.msgs.append({"role":"user","content":p})
        with st.chat_message("user"): st.markdown(p)
        r = f"Sobre {p} - preto e dourado é poder."
        with st.chat_message("assistant"): st.markdown(r)
        st.session_state.msgs.append({"role":"assistant","content":r})
