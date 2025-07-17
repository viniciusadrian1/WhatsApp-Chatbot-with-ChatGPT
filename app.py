from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from utils import responder_chatgpt, baixar_arquivo_audio, transcrever_audio_whisper
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    print("🔔 Webhook recebido!")

    try:
        num_media = request.values.get("NumMedia", "0")
        content_type = request.values.get("MediaContentType0", "")
        media_url = request.values.get("MediaUrl0", "")
        print("NumMedia:", num_media)
        print("MediaType:", content_type)
        print("MediaUrl:", media_url)

        if num_media != "0" and content_type.startswith("audio"):
            print("🎧 Áudio detectado, baixando e transcrevendo...")
            caminho_audio = baixar_arquivo_audio(media_url)
            mensagem_usuario = transcrever_audio_whisper(caminho_audio)
        else:
            mensagem_usuario = request.values.get("Body", "").strip()

        resposta = responder_chatgpt(mensagem_usuario)
        print("💬 Resposta:", resposta)

    except Exception as e:
        print("❌ Erro no webhook:", e)
        resposta = "Desculpe, houve um erro ao processar sua mensagem."

    twiml = MessagingResponse()
    twiml.message(resposta)
    return str(twiml)
