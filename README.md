# 🤖 ClassificAÍ

O ClassificAÍ foi desenvolvido com foco em **simplicidade, clareza e automação**, utilizando inteligência artificial para reduzir o trabalho manual na triagem de emails e apoiar equipes no dia a dia.

Ao automatizar a classificação e sugerir respostas adequadas, a solução contribui para **ganho de produtividade** e melhor aproveitamento do tempo das equipes.

Muitos emails na sua caixa de entrada?  

👉 *Deixa que o ClassificAÍ resolve.*

---

# 📧 Sobre o ClassificAÍ

ClassificAÍ é uma aplicação web que utiliza **IA via Groq (OpenAI-compatible API)** para **classificar emails corporativos** em *Produtivos* ou *Improdutivos* e **sugerir respostas automáticas profissionais**.

O projeto foi criado com foco em **boas práticas de desenvolvimento**, **prompt engineering**, **integração com LLMs** e uma abordagem **DevOps-friendly**, utilizando variáveis de ambiente e ambiente virtual isolado.

Ele foi desenvolvido como parte do **desafio de trainee da AutoU**, demonstrando habilidades em **Python, IA aplicada e automação de processos**.

---

## 🎯 Objetivo do Projeto

* Automatizar a triagem de emails corporativos
* Reduzir carga operacional de times administrativos e de suporte
* Demonstrar integração prática entre **Python + IA generativa**
* Servir como projeto de **desafio prático para trainee**, mostrando habilidades técnicas e de DevOps

---

## 🧠 Como a aplicação funciona

A aplicação envia o conteúdo do email para um **modelo LLM hospedado na Groq**, utilizando a API compatível com OpenAI (`/chat/completions`).

A IA recebe um **prompt estruturado**, instruindo-a a:

* Classificar o email como **Produtivo** ou **Improdutivo**
* Gerar uma resposta curta, educada e profissional
* Responder sempre em um formato padronizado

### Definições usadas no prompt

**Produtivo**:

* Solicitação de ação
* Suporte técnico
* Status de chamados
* Envio de documentos
* Dúvidas sobre sistemas ou processos

**Improdutivo**:

* Agradecimentos
* Felicitações
* Mensagens sociais
* Conteúdo reflexivo ou informativo sem necessidade de ação

---

## 🖥️ Funcionalidades

* 📄 Inserção de email via texto
* 📎 Upload de arquivos `.txt` e `.pdf`
* 🤖 Classificação automática com IA
* ✉️ Sugestão de resposta automática
* 🧪 Logs para depuração

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Flask** (backend web)
* **Groq API** (LLM)
* **Requests** (HTTP client)
* **PyPDF2** (leitura de PDFs)
* **python-dotenv** (variáveis de ambiente)

---

## 📦 Estrutura do Projeto

```
classificai/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── venv/
```

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
GROQ_API_KEY=gs_sua_chave_aqui
```

⚠️ **Nunca versionar o `.env`**

---

## 🚀 Como executar o projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

---

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Executar a aplicação

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 🧪 Exemplo de Email Produtivo

**Assunto:** Erro ao acessar o sistema de faturamento

> Desde hoje pela manhã estamos enfrentando erro 500 ao acessar o sistema de faturamento. O problema está impactando o fechamento das notas fiscais.

**Classificação:** Produtivo

**Resposta sugerida:**

> Agradecemos o contato. Nossa equipe técnica já foi acionada e está trabalhando na resolução do problema. Em breve retornaremos com uma atualização.

---

## 📄 Exemplo de Email Improdutivo

> Texto reflexivo sobre empatia e liderança, sem solicitação de ação.

**Classificação:** Improdutivo

**Resposta sugerida:**

> Agradecemos por compartilhar sua reflexão. É sempre enriquecedor receber conteúdos que incentivam o desenvolvimento humano e profissional.

---

## 📋 Dependências

As dependências estão listadas em `requirements.txt`, gerado a partir de um ambiente virtual isolado utilizando `pip freeze`, garantindo reprodutibilidade do ambiente.

---

## 🧩 Próximos Passos (Evolução)

* Autenticação de usuários
* Histórico de emails classificados
* Integração com SMTP / Gmail / Outlook
* Deploy em Docker
* Pipeline CI/CD

---

## 👤 Candidato

Este projeto foi desenvolvido como parte do **desafio de trainee da AutoU**, demonstrando habilidades em **Python, Flask, IA aplicada e automação de processos**.

---

## 📌 Observações

- A aplicação está funcional e pronta para testes.
- Todos os emails de exemplo e instruções estão no README.
- Para qualquer dúvida sobre execução ou funcionalidades, consulte a seção "Como executar o projeto".