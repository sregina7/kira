import streamlit as st
import os, urllib.parse, random, time

st.set_page_config(page_title="KIRA V15 - Preto e Dourado Luxo", page_icon="🦁", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Inter:wght@400;600&display=swap');

.stApp { background: #000000 !important; }

.main .block-container {
    background: #0a0a0a;
    border: 1px solid #8C6A2F;
    border-radius: 24px;
    padding: 2rem !important;
    box-shadow: 0 0 30px rgba(140,106,47,0.15);
}

/* KIRA - DOURADO METALICO REAL - NAO AMARELO */
h1 {
    font-family: 'Cinzel', serif !important;
    font-weight: 900 !important;
    text-align: center;
    letter-spacing: 10px;
    font-size: 3.8rem !important;
    margin-bottom: 0 !important;
    /* Dourado metálico degradê */
    background: linear-gradient(180deg, #E6C67A 0%, #D4AF37 25%, #8C6A2F 50%, #D4AF37 75%, #E6C67A 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    filter: drop-shadow(0 0 12px rgba(212,175,55,0.5)) drop-shadow(0 2px 2px rgba(0,0,0,0.8));
}

.subtitle {
    text-align: center;
    color: #8C6A2F;
    letter-spacing: 6px;
    font-size: 10px;
    font-family: 'Inter', sans-serif;
    margin-top: 8px;
    margin-bottom: 28px;
    font-weight: 600;
}

.stButton>button {
    background: linear-gradient(90deg, #8C6A2F 0%, #D4AF37 30%, #E6C67A 50%, #D4AF37 70%, #8C6A2F 100%) !important;
    color: #000 !important;
    border: 1px solid #5A441F !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    height: 52px;
    font-family: 'Inter', sans-serif;
    text-transform: uppercase;
    box-shadow: 0 4px 15px rgba(140,106,47,0.3);
}
.stButton>button:hover {
    box-shadow: 0 0 30px rgba(212,175,55,0.6) !important;
    transform: translateY(-1px);
}

.stTextArea textarea, .stTextInput input {
    background: #111 !important;
    border: 1px solid #8C6A2F !important;
    color: #E6C67A !important;
    border-radius: 12px !important;
}

div[data-testid="stTabs"] button {
    color: #8C6A2F !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #E6C67A !important;
    border-bottom: 2px solid #D4AF37 !important;
}
</style>
""", unsafe_allow_html=True)

def gerar_imagem_url(prompt):
    # Prompt fiel + toques pretos e dourados
    p = f"{prompt}, black and gold luxury tattoo design, golden details, black background, metallic gold ink, ultra detailed"
    enc = urllib.parse.quote(p)
    # Usa modelo turbo que é mais estável que flux no pollinations
    seed = random.randint(1,9999999)
    return f"https://image.pollinations.ai/prompt/{enc}?width=1024&height=1024&seed={seed}&nologo=true&model=turbo"

st.markdown("<h1>KIRA</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>V15 • PRETO E DOURADO • OFICIAL • LUXO</div>", unsafe_allow_html=True)

# Logo
logo_files = ["geometric_lioness_k_icon.jpg","logo.png","logo.jpg","geometric_lioness_k_icon.png","kira.png"]
found = None
for f in logo_files:
    if os.path.exists(f):
        found = f
        break
if found:
    c1,c2,c3 = st.columns([1,1.8,1])
    with c2:
        st.image(found, use_container_width=True)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

st.markdown("---")
t1, t2 = st.tabs(["GERAR IMAGEM FIEL", "CHAT KIRA"])

with t1:
    prompt = st.text_area("Descreva sua imagem fiel:", height=130, placeholder="Ex: dragão preto com borboleta dourada no nariz, estilo tattoo luxo...")
    if st.button("GERAR EM PRETO E DOURADO", use_container_width=True, key="gen"):
        if prompt and len(prompt) > 3:
            url = gerar_imagem_url(prompt)
            with st.spinner("KIRA está criando em preto e dourado..."):
                time.sleep(0.8)
                st.image(url, caption=prompt, use_container_width=True)
                st.markdown(f"[📥 Baixar imagem em alta]({url})")
            st.success("Imagem gerada fiel ao seu prompt!")
        else:
            st.warning("Escreva seu prompt, Sandra!")

with t2:
    if "msgs" not in st.session_state:
        st.session_state.msgs = [{"role":"assistant","content":"Sou a KIRA V15 em dourado metálico real 🦁\n\nAgora com ouro velho de verdade, não amarelo gema. O que vamos criar?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if p := st.chat_input("Fala com a Kira..."):
        st.session_state.msgs.append({"role":"user","content":p})
        with st.chat_message("user"):
            st.markdown(p)
        resp = f"Perfeito: {p}\n\nVou criar isso em preto e dourado metálico, luxo total, fiel ao que você pediu."
        with st.chat_message("assistant"):
            st.markdown(resp)
        st.session_state.msgs.append({"role":"assistant","content":resp})

st.markdown("---")
st.markdown("<div style='text-align:center; color:#8C6A2F; font-size:10px; letter-spacing:3px;'>KIRA V15 • Criada por Sandra Regina • San Art Tattoo • Dourado Metálico Oficial • 2026</div>", unsafe_allow_html=True)
