from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from utils import responder_chatgpt
import os

load_dotenv()
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    mensagem = request.form.get("Body")
    resposta = responder_chatgpt(mensagem)
    twiml = MessagingResponse()
    twiml.message(resposta)
    return str(twiml)

if __name__ == "__main__":
    app.run(debug=True)
