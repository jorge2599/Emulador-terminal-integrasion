import random
from colorama import init, Fore, Back
import os
from utilidades.Cuadro import mostrar_mensaje
from utilidades.Carga  import carga, circle_loader
from chatbot.Chat_bot import *
from juegos.Adivina_el_numero import adivinanum
from utilidades.Vida import barra, vida
from utilidades.Verificar_Vida import validar
from utilidades.Verificar_Vida import validar
from juegos.Piedra_Papel_Tijera import piedra_papel_tijera
from Matematicas.matematica import menu_opcion, matematicas, diametro
from interfas.menu_lista import  txt, menum, despedida, men
from utilidades.Comando import commad


barra_vida = barra()
carga("guardando vida")



def menu():
  print(Fore.YELLOW + txt)
  mostrar_mensaje(menum,Fore.CYAN)
  opcion = {
    "1": lambda: (carga("cargando juego", Fore.CYAN, 2),adivinanum(vida)),
    "2": lambda:(carga("cargando juego", Fore.CYAN, 2), piedra_papel_tijera()),
    "chat": lambda:(circle_loader(), chatbot()),
    "opcion": lambda:(carga("cargando menu", Fore.CYAN, 2), menu_opcion()),
    "terminal": lambda:(carga("cargando terminal", Fore.BLUE, 2), commad())
    
    
  }
  
  
  while True:
    player = input(Fore.CYAN + "=>").lower()
    if player == "vida":
        carga("verificando vida", Fore.CYAN, 1)
        print(f"{Fore.BLUE}vida[{barra_vida}]{vida}/10")
        continue
    elif player in ["salir","cerrar","adios"]:
       mostrar_mensaje(random.choice(despedida),Fore.BLUE)
       carga("cerrando programa",Fore.RED, 2)
       break
    elif player == "juegos" or player == "juego":
      carga()
      mostrar_mensaje(men,Fore.MAGENTA)
    elif player == "borra":
      #borra la terminal
      os.system('cls' if os.name == 'nt' else 'clear')
      menu()
    #ejecuta la funcion del diccionario 
    elif player in opcion:opcion[player]()#llama a la funcion correspondiente
    else:
      circle_loader()
        
      mostrar_mensaje("no es una opcion",Fore.RED)
      