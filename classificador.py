import os
import requests
from dotenv import load_dotenv

if os.environ.get("STREAMLIT_ENV") != "production":
    load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "").strip()

if not GROQ_API_KEY:
    if os.environ.get("STREAMLIT_ENV") == "production":
        raise ValueError("Chave da API Groq não encontrada! Verifique suas Secrets no Streamlit Cloud.")
    else:
        raise ValueError("Chave da API Groq não encontrada! Verifique seu arquivo .env")
    
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"

def classificar_com_ia(email_text):
    """
    Classifica um email corporativo usando a API Groq e sugere uma resposta automática.

    Parâmetros:
    email_text (str): Texto do email a ser classificado.

    Retorna:
    tuple: (categoria, resposta) onde:
        categoria (str) - "Produtivo" ou "Improdutivo"
        resposta (str) - resposta curta, educada e profissional
    """
    messages = [
        {
            "role": "system",
            "content": (
               "Você é um classificador de emails corporativos de uma empresa do setor financeiro.\n\n"
            "Classifique emails em:\n"
            "- Produtivo: emails que solicitam ação, suporte, status de solicitações,\n"
            "  envio de documentos, problemas técnicos ou dúvidas sobre sistemas/processos.\n"
            "- Improdutivo: emails de agradecimento, felicitações, mensagens sociais\n"
            "  ou que não exigem ação.\n\n"
            "Após classificar, gere uma resposta curta, educada e profissional.\n\n"
            "Sempre responda no formato:\n"
            "Categoria: <Produtivo ou Improdutivo>\n"
            "Resposta: <mensagem>"
            )
        },
        {"role": "user", "content": email_text}
    ]

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.2
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    response.raise_for_status()
    output = response.json()["choices"][0]["message"]["content"].strip()

    categoria, resposta = "", ""
    for line in output.split("\n"):
        if line.lower().startswith("categoria:"):
            categoria = line.split(":", 1)[1].strip()
        elif line.lower().startswith("resposta:"):
            resposta = line.split(":", 1)[1].strip()

    if not categoria:
        categoria = "Improdutivo"
    if not resposta:
        resposta = "Mensagem recebida, agradecemos seu contato."

    return categoria, resposta
