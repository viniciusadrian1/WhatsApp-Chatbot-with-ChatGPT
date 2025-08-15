# 🤖 ChatbotIA

ChatbotIA é um assistente inteligente com integração à API do ChatGPT, desenvolvido para aceitar entrada via texto e áudio. Ele foi criado com Python e Flask, oferecendo uma interface simples de interação por API.

ChatbotIA is an intelligent assistant with integration to the ChatGPT API, designed to accept input via text and audio. It was developed using Python and Flask, providing a simple API-based interaction interface.

**Autor:** Vinícius Adrian

## 🧠 Funcionalidades

- 💬 Entrada de texto: envie mensagens diretamente para o chatbot.
- 🎙️ Entrada de áudio: envie áudios (voz) e o sistema converte automaticamente para texto utilizando Whisper da OpenAI.
- 🧠 Integração com a API da OpenAI (ChatGPT) para respostas inteligentes.
- 🌐 API REST construída com Flask.
- ☁️ Pronto para deploy no Heroku.

## 🗂 Estrutura do Projeto

```
chatbotia-main/
│
├── app.py              # Arquivo principal que executa o servidor Flask
├── utils.py            # Funções auxiliares (ex: reconhecimento de voz)
├── requirements.txt    # Dependências do projeto
├── Procfile            # Arquivo de configuração para deploy no Heroku
└── .env                # Variáveis de ambiente (não incluído por padrão)
```

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/chatbotia-main.git
cd chatbotia-main
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` com o seguinte conteúdo:
```
OPENAI_API_KEY=sua-chave-aqui
```

## ▶️ Executando o projeto localmente

```bash
python app.py
```

A API estará disponível em `http://localhost:5000`.

## 📤 Endpoints da API

### `POST /chat`

- Envia uma mensagem de texto para o chatbot.
- **Body JSON:**
```json
{
  "message": "Olá, tudo bem?"
}
```

### `POST /audio`

- Envia um arquivo de áudio (formato WAV ou MP3).
- **Body:** multipart/form-data com campo `file`.

## 🚀 Deploy no Heroku

1. Faça login no Heroku:
```bash
heroku login
```

2. Crie o app:
```bash
heroku create nome-do-app
```

3. Faça o deploy:
```bash
git init
heroku git:remote -a nome-do-app
git add .
git commit -m "deploy"
git push heroku master
```

4. Adicione sua chave da OpenAI:
```bash
heroku config:set OPENAI_API_KEY=sua-chave-aqui
```

## 📌 Requisitos

- Python 3.7+
- Conta e chave de API da OpenAI
