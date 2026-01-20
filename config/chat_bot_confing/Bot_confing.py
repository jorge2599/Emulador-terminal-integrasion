import json
from chatbot.animaciones_del_bot.animacion_escritura_bot import efecto_maquina_de_escribir


#respuestas cargadas del json anteriormente py

with open("dato_info_txt/chat_bot_json/Dialogo.json", "r", encoding="UTF-8") as f:
    data = json.load(f)

    respuesta = data["respuesta"]
    info = data["info"]
    resp = data["ERROR"]
    ayuda= data["ayuda"]
    

with open("dato_info_txt/chat_bot_json/clave.json", "r", encoding="UTF-8") as f:
    clave = json.load(f)
    intencion = clave["intencion"]
    inform = clave["inform"]
    dato = clave["dato"]

    