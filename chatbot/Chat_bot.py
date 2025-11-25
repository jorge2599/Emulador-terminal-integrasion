from utilidades.Cuadro import mostrar_mensaje
from colorama import init, Fore
import random 
import sys
import time 
from utilidades.Carga import carga, circle_animation as animation
from datetime import datetime
from chatbot.Dialogo import respuesta as res, resp, des, inform, info, dato




def fecha():
  pass





def chatbot():
  mostrar_mensaje("chatbot en desarrollo", Fore.RED)
  while True:
      clave = input(Fore.BLUE + "==>").lower()
      
      #cierra chatbot
      if clave in dato:
        mostrar_mensaje(random.choice(des), Fore.CYAN)
        break

      #corversacion
      elif clave in res:
        animation(2, Fore.MAGENTA)
        texto = random.choice(res[clave])
        for char in texto:
          sys.stdout.write(Fore.CYAN + char)
          sys.stdout.flush()
          time.sleep(0.05)
        print()

        #informacion de capacidad
      elif clave in inform:
        mostrar_mensaje(info, Fore.GREEN)

        #en cas de quedar sin respuesta
      else:
        carga("analizando para entender", Fore.YELLOW, 2)
        mostrar_mensaje(random.choice(resp), Fore.CYAN)
  


  

  