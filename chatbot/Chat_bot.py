from utilidades.Cuadro import mostrar_mensaje
from colorama import init, Fore
import random 
import sys
import time 
from utilidades.Carga import carga, circle_animation as animation
from datetime import datetime
from chatbot.Bot_confing  import respuesta as res, resp, des, inform, info, dato
from config.confing import json_dato_version



def fecha():
  pass


def efecto_maquina_de_escribir(msj):
       for char in msj:
           sys.stdout.write(Fore.CYAN + char)
           sys.stdout.flush()
           time.sleep(0.05)
       print()


#json de las versiones del proyecto
def control_versiones_info():
    json_version = json_dato_version()
    nombre =  json_version["nombre"]
    version = json_version["version_actual"]
    return nombre, version
nombre, version =control_versiones_info()

#logica del chatbot
def chatbot():
  mostrar_mensaje("chatbot en desarrollo", Fore.RED)
  while True:
      clave = input(Fore.BLUE + "==>").lower()
      
      #cierra chatbot
      if clave in dato:
        efecto_maquina_de_escribir(des)
        break

      #conversacion
      elif clave in res:
        animation(2, Fore.MAGENTA)
        texto = random.choice(res[clave])
        efecto_maquina_de_escribir(texto)

        #informacion de capacidad
      elif clave in inform:
        mostrar_mensaje(info, Fore.GREEN)


      elif clave == "version":
          mostrar_mensaje(Fore.CYAN + version)
      

        #en caso de quedar sin respuesta
      else:
        carga("analizando para entender", Fore.YELLOW, 2)
        mostrar_mensaje(random.choice(resp), Fore.CYAN)
  


  

  
