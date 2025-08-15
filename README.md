# 🤖 ChatbotIA

**PT:** ChatbotIA é um assistente inteligente com integração à API do ChatGPT, que aceita entradas de texto e áudio. Desenvolvido em Python e Flask, oferece uma interface simples via API.  
**EN:** ChatbotIA is an intelligent assistant integrated with the ChatGPT API, accepting text and audio inputs. Built with Python and Flask, it provides a simple API-based interface.

**Autor / Author:** Vinícius Adrian

---

## 🧠 Funcionalidades / Features

- 💬 **Texto / Text:** envie mensagens diretamente / send messages directly.  
- 🎙️ **Áudio / Audio:** converte voz em texto usando OpenAI Whisper / converts voice to text using OpenAI Whisper.  
- 🧠 **IA / AI:** respostas inteligentes via ChatGPT / intelligent responses via ChatGPT.  
- 🌐 **API REST:** construída com Flask / built with Flask.  
- ☁️ **Deploy:** pronto para Heroku / ready for Heroku deployment.

---

## 🗂 Estrutura do Projeto / Project Structure

```
chatbotia-main/
├── app.py          # Servidor Flask principal / Main Flask server
├── utils.py        # Funções auxiliares / Helper functions
├── requirements.txt# Dependências / Dependencies
├── Procfile        # Configuração Heroku / Heroku config
└── .env            # Variáveis de ambiente / Environment variables
```

---

## ⚙️ Instalação / Installation

```bash
git clone https://github.com/seu-usuario/chatbotia-main.git
cd chatbotia-main
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

Crie o arquivo `.env` com sua chave da OpenAI:  
```
OPENAI_API_KEY=sua-chave-aqui / your-api-key-here
```

---

## ▶️ Executando / Running Locally

```bash
python app.py
```
A API estará disponível em `http://localhost:5000` / The API will be available at `http://localhost:5000`.

---

## 📤 Endpoints da API / API Endpoints

### `POST /chat`
- **Descrição / Description:** Envia mensagem de texto / Sends text message.  
- **Exemplo / Example:**
```json
{
  "message": "Olá, tudo bem?" / "Hello, how are you?"
}
```

### `POST /audio`
- **Descrição / Description:** Envia arquivo de áudio (WAV/MP3) / Sends audio file (WAV/MP3).  
- **Body:** multipart/form-data com campo `file` / multipart/form-data with `file` field.

---

## 🚀 Deploy no Heroku / Heroku Deployment

```bash
heroku login
heroku create nome-do-app / app-name
git init
heroku git:remote -a nome-do-app / app-name
git add .
git commit -m "deploy"
git push heroku master
heroku config:set OPENAI_API_KEY=sua-chave-aqui / your-api-key-here
```

---

## 📌 Requisitos / Requirements

- Python 3.7+  
- Conta e chave de API da OpenAI / OpenAI account and API key
