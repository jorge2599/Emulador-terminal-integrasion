from colorama import init, Fore, Style
import random 
import sys
import time 
from utilidades.Carga import carga, circle_animation as animation
from utilidades.Cuadro import mostrar_mensaje
from utilidades.calendario import *
from datetime import datetime
from chatbot.Bot_confing  import respuesta as res, resp, des, inform, info, dato,intencion, ayuda, efecto_maquina_de_escribir
from config.confing import json_dato_version

init(autoreset=True)




#logica del chatbot
def chatbot():
  mostrar_mensaje("chatbot en desarrollo", Fore.RED)
  while True:
      clave = input("==>").lower()
      
      #cierra chatbot
      if clave in dato:
        efecto_maquina_de_escribir(des, Fore.BLUE)
        break

      #conversacion
      elif clave in res:
        animation(2)
        efecto_maquina_de_escribir(random.choice(res[clave]), Fore.BLUE)

        #informacion de capacidad
      elif clave in inform:
        efecto_maquina_de_escribir(info, Fore.BLUE)

      elif clave in intencion:
          respuesta = ayuda[intencion[clave]].format(
        nombre=json_dato_version()["nombre"],
        estado=json_dato_version()["estado"],
        version=json_dato_version()["version_actual"],
        descripcion=json_dato_version()["descripcion"]
    )

          efecto_maquina_de_escribir(respuesta, Fore.BLUE)
          
        #en caso de quedar sin respuesta
      else:
        carga("analizando para entender")
        efecto_maquina_de_escribir(random.choice(resp), Fore.BLUE)
  


  

  
