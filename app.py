from flask import Flask, render_template, request
import PyPDF2
import os
import requests
from dotenv import load_dotenv

# 🔹 Carrega variáveis de ambiente
load_dotenv()

print("GROQ_API_KEY carregada?", bool(os.getenv("GROQ_API_KEY")))

app = Flask(__name__)

# 🔹 Configuração Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"


def classificar_com_ia(email_text):
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
        {
            "role": "user",
            "content": email_text
        }
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

    print("Status code:", response.status_code)
    print("Resposta bruta:", response.text)

    response.raise_for_status()

    result = response.json()
    output = result["choices"][0]["message"]["content"].strip()

    categoria = ""
    resposta = ""

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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def classify_email():
    email_text = request.form.get("email_text")
    email_file = request.files.get("email_file")

    if email_file:
        filename = email_file.filename.lower()
        if filename.endswith(".txt"):
            email_text = email_file.read().decode("utf-8")
        elif filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(email_file)
            email_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    email_text += text + "\n"
        else:
            email_text = ""

    email_text = email_text.strip() if email_text else ""

    if email_text:
        categoria, resposta = classificar_com_ia(email_text)
    else:
        categoria = "Sem conteúdo"
        resposta = "Nenhum email fornecido ou arquivo inválido."

    return render_template(
        "index.html",
        categoria=categoria,
        resposta=resposta,
        email_text=email_text
    )


if __name__ == "__main__":
    app.run(debug=True)
