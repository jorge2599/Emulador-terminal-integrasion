from colorama import init, Fore, Style
import random 
import sys
import time 
from utilidades.Carga import carga, circle_animation as animation
from utilidades.Cuadro import mostrar_mensaje
from utilidades.calendario import *
from datetime import datetime
from config.chat_bot_confing.Bot_confing  import respuesta as res,resp, inform, info, dato,intencion, ayuda, efecto_maquina_de_escribir
from config.confing import json_dato_version

init(autoreset=True)
VERDE_LIMA_NEON = "\033[1;38;2;128;247;55m"
Rosa_Neon = "\033[1;38;2;250;88;185m"
RESET = "\033[0m"



#logica del chatbot
def chatbot():
  mostrar_mensaje("chatbot en desarrollo", Fore.RED)
  while True:
      clave = input(Rosa_Neon + "==>" ).lower()
      
      #cierra chatbot
      if clave in dato:
        efecto_maquina_de_escribir(random.choice(res["despedida"]), VERDE_LIMA_NEON)
        break

      #conversacion
      elif clave in res:
        animation(2)
        efecto_maquina_de_escribir(random.choice(res[clave]), VERDE_LIMA_NEON)

        #informacion de capacidad
      elif clave in inform:
        efecto_maquina_de_escribir(info, VERDE_LIMA_NEON)

      elif clave in intencion:
          respuesta = ayuda[intencion[clave]].format(
        nombre=json_dato_version()["nombre"],
        estado=json_dato_version()["estado"],
        version=json_dato_version()["version_actual"],
        descripcion=json_dato_version()["descripcion"]
    )

          efecto_maquina_de_escribir(respuesta, VERDE_LIMA_NEON)
          
        #en caso de quedar sin respuesta
      else:
        carga("analizando para entender")
        efecto_maquina_de_escribir(random.choice(resp), VERDE_LIMA_NEON)
  


  

  
