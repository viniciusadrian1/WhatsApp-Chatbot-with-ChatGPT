from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def responder_chatgpt(mensagem):
    prompt = f"""
Você é o assistente da BeyondBox, uma empresa que vende caixas cartonadas e produtos personalizados como canecas, camisetas e copos. Responda com simpatia e objetividade:
'{mensagem}'
"""
    resposta = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um atendente da BeyondBox."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta.choices[0].message.content.strip()
