import streamlit as st
import PyPDF2
from dotenv import load_dotenv
from classificador import classificar_com_ia  # Importando a função do outro arquivo

load_dotenv()

st.set_page_config(page_title="ClassificAÍ", page_icon="✉️", layout="centered")
st.title("🤖 ClassificAÍ")
st.subheader("Classificação inteligente de emails")

uploaded_file = st.file_uploader("Envie um arquivo (.txt ou .pdf)", type=["txt", "pdf"])
email_text_input = st.text_area("Ou cole o conteúdo do email aqui:")

if st.button("Classificar Email"):
    email_text = email_text_input.strip() if email_text_input else ""

    if uploaded_file:
        filename = uploaded_file.name.lower()
        if filename.endswith(".txt"):
            email_text = uploaded_file.read().decode("utf-8")
        elif filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(uploaded_file)
            email_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    email_text += text + "\n"

    if email_text:
        categoria, resposta = classificar_com_ia(email_text)
        st.subheader("📌 Resultado")
        st.markdown(f"**Categoria:** {categoria}")
        st.markdown(f"**Resposta sugerida:** {resposta}")
        st.markdown("**Texto do email:**")
        st.code(email_text)
    else:
        st.warning("Nenhum conteúdo fornecido. Insira um email ou faça upload de um arquivo.")
