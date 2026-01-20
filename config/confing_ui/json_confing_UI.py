import json

with open("dato_info_txt/UI_Clave_json/Clave_dato_Comando.json", "r", encoding="utf-8") as f:
    Clave_dato_Comando = json.load(f)
    

clear = Clave_dato_Comando["clear"]