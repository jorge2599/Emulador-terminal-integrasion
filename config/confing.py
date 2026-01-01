import  json

def json_dato_version():
    with open("config/version.json", "r", encoding="utf-8") as f:
         data = json.load(f)
    return data
