import os
import openai
import requests
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def baixar_arquivo_audio(url):
    print("🔽 Baixando:", url)
    r = requests.get(url, auth=(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")))
    caminho = "audio_recebido.ogg"
    with open(caminho, "wb") as f:
        f.write(r.content)
    return caminho

def transcrever_audio_whisper(caminho):
    print("📝 Transcrevendo:", caminho)
    with open(caminho, "rb") as audio:
        transcricao = openai.Audio.transcribe("whisper-1", audio)
    return transcricao["text"]

def responder_chatgpt(mensagem):
    print("🤖 Enviando para o GPT:", mensagem)
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": mensagem }]
    )
    return resposta.choices[0].message.content.strip()
