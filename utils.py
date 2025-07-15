from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def responder_chatgpt(mensagem):
    prompt = f"""
Você é um atendente da Roupa de Cheiro, uma empresa que vende caixas cartonadas e produtos personalizados como canecas, camisetas e copos. Responda com simpatia e objetividade:
'{mensagem}'
"""
    resposta = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um atendente da Roupa de Cheiro."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta.choices[0].message.content.strip()


import requests
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def baixar_arquivo_audio(url, caminho="audio_recebido.ogg"):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(caminho, "wb") as f:
            f.write(resposta.content)
        return caminho
    else:
        raise Exception("Falha ao baixar o áudio")

def transcrever_audio_whisper(caminho_audio):
    with open(caminho_audio, "rb") as audio_file:
        transcricao = openai.Audio.transcribe("whisper-1", audio_file)
    return transcricao["text"]
