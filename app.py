import streamlit as st

st.set_page_config(
    page_title="KIRA - San Art Tattoo",
    page_icon="🖤",
    layout="centered"
)

# Estilo San Art Tattoo
st.markdown("""
<style>
    .main { background-color: #0a0a0a; }
    .stChatMessage { border-radius: 15px; }
    h1 { color: #D4AF37; text-align: center; }
    .subtitle { text-align: center; color: #888; }
</style>
""", unsafe_allow_html=True)

st.markdown("# KIRA - San Art Tattoo 🖤")
st.markdown('<p class="subtitle">Sua assistente virtual - Cria descrições de tattoo em PT e EN<br>Funciona 24h no celular, iPad e PC</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Oi! Eu sou a KIRA do San Art Tattoo! 🖤✨ Me conta sua ideia de tatuagem que eu crio a descrição perfeita em Português e Inglês pra você levar pro tatuador!"}
    ]

def kira_resposta(mensagem):
    msg = mensagem.lower()
    
    if any(p in msg for p in ["tattoo", "tatuagem", "ideia", "desenho", "quero fazer"]):
        return f"""🖤 **Ideia anotada: {mensagem}**

**Descrição PT (para briefing):**
Tatuagem com conceito de '{mensagem}', estilo delicado e autoral, linhas finas, acabamento minimalista, perfeita para o estúdio San Art Tattoo.

**Description EN (for artist):**
Tattoo concept: '{mensagem}', delicate and original style, fine lines, minimalist finish, perfect for San Art Tattoo studio.

Quer que eu refine? Me fala o local do corpo e o tamanho!"""

    elif any(p in msg for p in ["preço", "valor", "quanto", "price", "cost"]):
        return """💰 **Sobre valores San Art Tattoo:**

Valores dependem de tamanho, local e detalhes. Me chama no Whats do estúdio com a ideia que já deixei pronta que te passo o orçamento!

Enquanto isso, qual sua ideia? Já deixo a descrição bilíngue pronta pra você!"""

    elif any(p in msg for p in ["traduz", "translate", "inglês", "português"]):
        return f"""🌎 **Tradução KIRA:**

**PT:** {mensagem}
**EN:** Tattoo idea: {mensagem} - delicate, minimalist style

Quer que eu melhore a descrição?"""

    elif any(p in msg for p in ["hello", "hi", "hey"]):
        return f"Hello! I'm KIRA from San Art Tattoo! 🖤 You said: '{mensagem}'. Tell me your tattoo idea and I'll create the perfect PT/EN description!"
    
    else:
        return f"""✨ Entendi: **'{mensagem}'**

Sou a KIRA! Posso:
1. Criar descrição da sua tattoo em PT e EN
2. Traduzir sua ideia
3. Sugerir estilos (minimalista, blackwork, fine line)

Me conta mais sobre sua ideia?"""

# Mostra histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Digite sua ideia de tatuagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    resposta = kira_resposta(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})

st.markdown("---")
st.markdown('<p style="text-align:center; color:#555; font-size:12px;">KIRA v1.0 - Independente - San Art Tattoo | São Paulo</p>', unsafe_allow_html=True)
