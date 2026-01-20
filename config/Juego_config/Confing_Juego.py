import json
from config.confing_ui.UI_utils import (mostrar_mensaje, carga, circle_loader, barra, vida, limpio)


with open("dato_info_txt/Juego_json/Juego_Dialogo.json", "r", encoding="utf-8") as f:
         data = json.load(f)
         res = data["respuesta"]
         gde = data["grande"]
         chc = data["chico"]
         respuestas_invalidas = data["INCORRECTO"]