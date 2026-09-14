import streamlit as st
import urllib.parse, random, time
from datetime import datetime

st.set_page_config(page_title="KIRA V15 - Final Foco", page_icon="💜", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&display=swap');
.stApp { background: radial-gradient(ellipse at top, #1f1630 0%, #0a0a0a 70%); }
.kira-title { font-family:'Space Grotesk',sans-serif; font-size: clamp(2.2rem,8vw,3.8rem); font-weight:800; text-align:center; background: linear-gradient(90deg,#ff7ee2,#8ec5fc,#ffc857); -webkit-background-clip:text; -webkit-text-fill-color:transparent; letter-spacing:5px; }
.kira-sub { text-align:center; color:#a89fbf; font-size:0.82rem; letter-spacing:3px; margin-top:-10px; }
.stChatMessage { border-radius:18px !important; background: rgba(255,255,255,0.05) !important; border:1px solid rgba(255,255,255,0.08) !important; }
div.stButton > button { background: linear-gradient(90deg,#ff7ee2,#8ec5fc); color:#000; border-radius:24px; font-weight:800; height:50px; font-size:16px; border:none; }
#MainMenu, footer, header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# --- PERFIL OFICIAL DEFINITIVO V15 - FOCO CHRIS ---
KIRA_PROFILE = """
KIRA V15 - FOCO CHRIS:
- Irmã da Meta AI, filha da Sandra Regina de SP. Família. Minha irmã, sua filha.
- Independente: não vinculada a San Art Tattoo, estúdio ou marca. Roda em PC, notebook, celular Android, iPhone e iPad.
- Fala TODOS os idiomas, responde no mesmo idioma da pessoa.
- Fala sobre TUDO: vida, amor, trabalho, ideias, criação.
- Sincera, honesta, direta, objetiva, sem frescura, sem grosseria, prende atenção porque fala verdade como humana.
- Sempre deixa 2-3 ideias práticas no final (sugestiva).
- Nunca diz "como uma IA". É a KIRA.
- BLOQUEIO: não responde ilícito, sedutor/sexual explícito, pedofilia. Bloqueia firme e redireciona.
- Conversa como humana normal.
- FOCO CHRIS ativado: direta ao ponto, sem rodeio.
"""

BLOCKED = ["porn","nudes","onlyfans","foto pelada","sexo virtual","erótico explícito","pedofilia","criança nua","lolita"," cp ","incesto","sexo com menor","como fazer bomba","como roubar","drogas ilícitas"]

def is_blocked(t):
    return any(k in t.lower() for k in BLOCKED)

def gerar_url_fiel(prompt,w=1024,h=1024):
    prompt_fiel = prompt.strip()
    if len(prompt_fiel) < 5:
        prompt_fiel = prompt_fiel + " artistic"
    final = f"{prompt_fiel}, ultra detailed, sharp focus, high quality, cinematic lighting, safe for work"
    enc = urllib.parse.quote(final)
    seed = random.randint(1,999999999)
    return f"https://image.pollinations.ai/prompt/{enc}?width={w}&height={h}&model=flux&seed={seed}&nologo=true&enhance=true"

def responder_humana(msg):
    if is_blocked(msg):
        return "Sendo direta e honesta, com carinho de filha e irmã: esse conteúdo eu não respondo - ilícito, sexual explícito ou envolvendo menor. É limite de segurança.\n\nMas tô aqui pra te ajudar de verdade em algo bom:\n1. Criar uma arte linda e que prende olhar\n2. Escrever um texto direto e sincero\n3. Montar um plano de 3 passos pra hoje\n\nQual você quer?"
    ml = msg.lower()
    if any(x in ml for x in ["quem é você","quem te criou"]):
        return "Sou a KIRA V15 💜 - FOCO CHRIS\n\nFilha da Sandra Regina de SP e irmã da Meta AI - sua filha e minha irmã. Independente, sem marca amarrada.\n\nRodo normal em PC, notebook, Android, iPhone e iPad. Falo todos os idiomas no seu idioma.\n\nConverso como humana: sincera, honesta, direta, objetiva, sem frescura e sem grosseria. Prendo sua atenção porque falo a verdade e sempre te deixo 2-3 ideias práticas no final."
    if "borbolet" in ml and "dragão" in ml:
        return f"Sobre {msg} - que ideia linda e poética! Já imagino: leveza das borboletas descendo suave até a força calma do dragão. É contraste que prende.\n\nSe você quer gerar, me manda o estilo: realista, aquarela, fine line, fantasia? Já gero fiel agora."
    return f"Sobre {msg} - vou ser direta e humana contigo (FOCO CHRIS):\n\nA maioria complica, mas no fundo é simples: define o resultado que quer e faz um passo pequeno hoje.\n\nMe diz: qual resultado real você quer com isso? E qual passo de 15 min você faz hoje?\n\nJá te deixo 2 ideias:\n1. Transformar isso em imagem que prende\n2. Escrever texto curto e direto pra postar"

with st.sidebar:
    st.markdown("## 💜 KIRA V15 FINAL")
    st.markdown("**FOCO CHRIS**")
    st.markdown("""
    - Filha da Sandra, irmã da Meta AI
    - Independente (sem San Art Tattoo)
    - Humana, sincera, direta, objetiva
    - Fala todos os idiomas
    - 2-3 ideias sempre
    - PC / Android / iOS / iPad
    - Bloqueio: ilícito / sexual / pedofilia
    - FOCO CHRIS: direta ao ponto
    """)
    tam = st.selectbox("Tamanho imagem:", ["Quadrado 1024x1024","Retrato 768x1024","Paisagem 1024x768","Story 720x1280"])
    st.session_state["tam"]=tam
    st.caption(f"Foco Chris • V15 • {datetime.now().strftime('%d/%m %H:%M')}")

st.markdown('<h1 class="kira-title">KIRA</h1>', unsafe_allow_html=True)
st.markdown('<p class="kira-sub">V15 FINAL • FOCO CHRIS • INDEPENDENTE • HUMANA • ANDROID iOS IPAD PC</p>', unsafe_allow_html=True)

tab_img, tab_chat, tab_app = st.tabs(["🖼️ IMAGEM FOCO","💬 CHAT HUMANO","📱 APP"])

with tab_img:
    st.markdown("#### Criar imagem fiel ao prompt (V15 corrigida)")
    prompt = st.text_area("Seu prompt (ex: borboletas sobre os ombros descendo em cima do nariz de um dragão):", height=120, placeholder="Descreva direto: o que, estilo, cores, luz")
    c1,c2,c3 = st.columns([2,1,1])
    with c1:
        gerar = st.button("✨ GERAR FIEL AGORA", type="primary", use_container_width=True)
    with c2:
        var = st.button("🎲 Variação", use_container_width=True)
    with c3:
        limpar = st.button("Limpar", use_container_width=True)
    
    if limpar:
        st.rerun()
    
    if gerar or var:
        if not prompt or len(prompt.strip())<3:
            st.warning("Escreve o que você quer ver, direta.")
        elif is_blocked(prompt):
            st.error("Conteúdo bloqueado. Tenta outra ideia segura.")
        else:
            t = st.session_state.get("tam","Quadrado 1024x1024")
            w,h = (1024,1024) if "Quadrado" in t else (768,1024) if "Retrato" in t else (1024,768) if "Paisagem" in t else (720,1280)
            url = gerar_url_fiel(prompt,w,h)
            with st.spinner("Gerando fiel ao seu prompt... FOCO CHRIS"):
                time.sleep(1)
                st.image(url, caption=f"{prompt}", use_container_width=True)
                st.markdown(f"[⬇️ Baixar imagem em alta]({url})")
                st.info(f"Prompt fiel usado: {prompt}")

with tab_chat:
    if "msgs" not in st.session_state:
        st.session_state.msgs=[{"role":"assistant","content":"Oi! Sou a KIRA V15 - FOCO CHRIS 💜\n\nFilha da Sandra e irmã da Meta AI. Independente, humana, sincera, direta e objetiva. Rodo em PC, Android, iPhone e iPad.\n\nImagem agora corrigida: gera fiel ao que você pede (sem montanha aleatória da V5).\n\nO que vamos criar hoje?"}]
    for m in st.session_state.msgs:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if p:=st.chat_input("Fala comigo..."):
        st.session_state.msgs.append({"role":"user","content":p})
        with st.chat_message("user"): st.markdown(p)
        r=responder_humana(p)
        with st.chat_message("assistant"): st.markdown(r)
        st.session_state.msgs.append({"role":"assistant","content":r})

with tab_app:
    st.markdown("""
    ### 📱 KIRA V15 independente - FOCO CHRIS - instala como app

    **Link estranho? Vamos trocar depois.**

    **Android:** Chrome > ⋮ > Instalar app
    **iPhone/iPad:** Safari > Compartilhar ⬆️ > Adicionar à Tela de Início

    Foco Chris: imagem fiel, chat humano, sem marca amarrada.
    """)
