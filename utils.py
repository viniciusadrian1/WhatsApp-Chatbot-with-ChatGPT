import os
import requests
from dotenv import load_dotenv
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def baixar_arquivo_audio(url):
    print("🔽 Baixando:", url)
    r = requests.get(url, auth=(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")))
    caminho = "audio_recebido.ogg"
    with open(caminho, "wb") as f:
        f.write(r.content)
    return caminho

def transcrever_audio_whisper(caminho):
    print("📝 Transcrevendo:", caminho)
    with open(caminho, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text

def responder_chatgpt(mensagem):
    print("🤖 Enviando para o GPT:", mensagem)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": mensagem }]
    )
    return response.choices[0].message.content.strip()
