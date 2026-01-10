import json
from chatbot.animaciones_del_bot.animacion_escritura_bot import efecto_maquina_de_escribir


#respuestas cargadas del json anteriormente py

with open("chatbot/Dialogo.json", "r", encoding="UTF-8") as f:
    data = json.load(f)

    respuesta = data["respuesta"]
    info = data["info"]
    resp = data["resp"]
    des = data["des"]
    inform = data["inform"]
    dato = data["dato"]
    ayuda= data["ayuda"]
    intencion = data["intencion"]


    