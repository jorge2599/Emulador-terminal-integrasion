import json

with open("chatbot/Dialogo.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    respuesta = data["respuesta"]
    info = data["info"]
    resp = data["resp"]
    des = data["des"]
    inform = data["inform"]
    dato = data["dato"]
