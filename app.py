import streamlit as st
import os, urllib.parse, random

st.set_page_config(page_title="KIRA V15 • Preto e Dourado", page_icon="🦁", layout="centered")

# CSS PREMIUM PRETO E DOURADO - CORRIGIDO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@800&family=Inter:wght@400;600&display=swap');

.stApp {
    background: #000000 !important;
}
.main .block-container {
    background: #0a0a0a;
    border: 1px solid #D4AF37;
    border-radius: 24px;
    padding: 2rem !important;
    box-shadow: 0 0 40px rgba(212,175,55,0.15);
    margin-top: 2rem;
}
h1 {
    font-family: 'Cinzel', serif !important;
    color: #FFD700 !important;
    text-align: center;
    letter-spacing: 8px;
    font-size: 3.5rem !important;
    margin-bottom: 0px !important;
    text-shadow: 0 0 20px rgba(255,215,0,0.5);
}
.subtitle {
    text-align: center;
    color: #B8941F;
    letter-spacing: 5px;
    font-size: 12px;
    font-family: 'Inter', sans-serif;
    margin-bottom: 25px;
    margin-top: -5px;
}
.stButton>button {
    background: linear-gradient(90deg, #D4AF37 0%, #FFD700 50%, #D4AF37 100%) !important;
    color: #000 !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    height: 50px;
    font-family: 'Inter', sans-serif;
    transition: 0.3s;
}
.stButton>button:hover {
    box-shadow: 0 0 25px #FFD700 !important;
    transform: scale(1.02);
}
.stTextArea textarea, .stTextInput input {
    background: #111 !important;
    border: 1px solid #D4AF37 !important;
    color: #FFD700 !important;
    border-radius: 12px !important;
}
.stChatMessage {
    background: #111 !important;
    border: 1px solid rgba(212,175,55,0.3) !important;
    border-radius: 16px !important;
}
div[data-testid="stSidebar"] {
    background: #050505 !important;
    border-right: 1px solid #D4AF37;
}
#MainMenu, footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

def gerar_imagem_url(prompt):
    p = f"{prompt}, black and gold luxury, golden details, black background, ultra detailed, photorealistic, 8k, cinematic lighting"
    enc = urllib.parse.quote(p)
    return f"https://image.pollinations.ai/prompt/{enc}?width=1024&height=1024&model=flux&seed={random.randint(1,999999)}&nologo=true"

# HEADER
st.markdown("<h1>KIRA</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>V15 • PRETO E DOURADO • OFICIAL • LUXO</div>", unsafe_allow_html=True)

# LOGO - procura em vários nomes
logo_files = ["logo.png","logo.jpg","geometric_lioness_k_icon.jpg","geometric_lioness_k_icon.png","kira.png"]
found = None
for f in logo_files:
    if os.path.exists(f):
        found = f
        break

if found:
    c1,c2,c3 = st.columns([1,2,1])
    with c2:
        st.image(found, use_container_width=True)
else:
    st.warning("Logo não encontrada. Suba geometric_lioness_k_icon.jpg como logo.png")

st.markdown("---")

# TABS
t1, t2 = st.tabs(["🖼️ GERAR IMAGEM FIEL", "💬 CHAT KIRA"])

with t1:
    prompt = st.text_area("Descreva sua imagem (fiel ao que escrever):", height=120, placeholder="Ex: borboletas douradas sobre os ombros descendo até o nariz de um dragão preto com olhos dourados...")
    if st.button("✨ GERAR EM PRETO E DOURADO", use_container_width=True):
        if prompt and len(prompt) > 3:
            url = gerar_imagem_url(prompt)
            st.image(url, caption=prompt, use_container_width=True)
            st.markdown(f"[📥 Baixar imagem]({url})")
            st.success("Imagem gerada fiel ao seu prompt!")
        else:
            st.warning("Escreva seu prompt")

with t2:
    if "msgs" not in st.session_state:
        st.session_state.msgs = [{"role":"assistant","content":"Sou a KIRA V15 em preto e dourado 🖤💛\n\nCriei pra você com luxo total. O que vamos criar agora?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if p := st.chat_input("Fala com a Kira..."):
        st.session_state.msgs.append({"role":"user","content":p})
        with st.chat_message("user"): st.markdown(p)
        resp = f"Entendi: {p}\n\nVamos fazer em preto e dourado, luxo e poder. Me fala mais detalhes que eu gero fiel."
        with st.chat_message("assistant"): st.markdown(resp)
        st.session_state.msgs.append({"role":"assistant","content":resp})

st.markdown("---")
st.markdown("<div style='text-align:center; color:#B8941F; font-size:11px; letter-spacing:2px;'>KIRA V15 • Criada por Sandra Regina • San Art Tattoo • Preto e Dourado Oficial • 2026</div>", unsafe_allow_html=True)
