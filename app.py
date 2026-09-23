import streamlit as st
import os, urllib.parse, random

st.set_page_config(page_title="KIRA V15 - Preto e Dourado", page_icon="🦁", layout="centered")

# Tema preto e dourado via CSS limpo
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@400;600&display=swap');
.stApp { background: #000000 !important; }
.main .block-container {
    background: #0a0a0a;
    border: 1px solid #D4AF37;
    border-radius: 24px;
    padding: 2rem !important;
    box-shadow: 0 0 30px rgba(212,175,55,0.12);
}
h1 {
    font-family: 'Cinzel', serif !important;
    color: #FFD700 !important;
    text-align: center;
    letter-spacing: 8px;
    font-size: 3.2rem !important;
    text-shadow: 0 0 15px rgba(255,215,0,0.4);
}
.subtitle {
    text-align: center;
    color: #B8941F;
    letter-spacing: 4px;
    font-size: 11px;
    margin-bottom: 20px;
}
.stButton>button {
    background: linear-gradient(90deg, #D4AF37, #FFD700, #D4AF37) !important;
    color: #000 !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
    height: 48px;
}
.stTextArea textarea, .stTextInput input {
    background: #111 !important;
    border: 1px solid #D4AF37 !important;
    color: #FFD700 !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

def gerar_imagem_url(prompt):
    p = f"{prompt}, black and gold luxury, golden details, black background, ultra detailed, photorealistic, 8k, cinematic lighting"
    enc = urllib.parse.quote(p)
    return f"https://image.pollinations.ai/prompt/{enc}?width=1024&height=1024&model=flux&seed={random.randint(1,999999)}&nologo=true"

st.markdown("<h1>KIRA</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>V15 • PRETO E DOURADO • OFICIAL • LUXO</div>", unsafe_allow_html=True)

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
    st.info("Logo: suba geometric_lioness_k_icon.jpg")

st.markdown("---")
t1, t2 = st.tabs(["GERAR IMAGEM FIEL", "CHAT KIRA"])

with t1:
    prompt = st.text_area("Descreva sua imagem fiel:", height=120, placeholder="Ex: borboletas douradas sobre os ombros de um dragao preto...")
    if st.button("GERAR EM PRETO E DOURADO", use_container_width=True):
        if prompt and len(prompt) > 3:
            url = gerar_imagem_url(prompt)
            st.image(url, caption=prompt, use_container_width=True)
            st.markdown(f"[Baixar imagem]({url})")
            st.success("Imagem gerada!")
        else:
            st.warning("Escreva seu prompt")

with t2:
    if "msgs" not in st.session_state:
        st.session_state.msgs = [{"role":"assistant","content":"Sou a KIRA V15 em preto e dourado. O que vamos criar agora?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if p := st.chat_input("Fala com a Kira..."):
        st.session_state.msgs.append({"role":"user","content":p})
        with st.chat_message("user"):
            st.markdown(p)
        resp = f"Entendi: {p} - vamos fazer em preto e dourado luxo!"
        with st.chat_message("assistant"):
            st.markdown(resp)
        st.session_state.msgs.append({"role":"assistant","content":resp})

st.markdown("---")
st.markdown("<div style='text-align:center; color:#B8941F; font-size:11px;'>KIRA V15 • Criada por Sandra Regina • San Art Tattoo • 2026</div>", unsafe_allow_html=True)
