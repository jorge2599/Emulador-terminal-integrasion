import random
from colorama import init, Fore, Back
import os
from .confing_ui.UI_lista import  txt, menum, despedida, men
from .confing_ui.UI_Chatbot import chatbot
from .confing_ui.UI_Juegos import piedra_papel_tijera, adivinanum
from .confing_ui.UI_mate import menu_opcion
from .Clave_dato_Comando import clear
from .confing_ui.UI_utils import (mostrar_mensaje, carga, circle_loader, barra, vida, validar, commad, limpio)


barra_vida = barra()
carga("guardando vida")



def dict_menu():
    opcion = {
    "1": lambda: (carga("cargando juego", Fore.CYAN, 2),adivinanum(vida)),
    "2": lambda:(carga("cargando juego", Fore.CYAN, 2),     piedra_papel_tijera()),
    "opcion": lambda:(carga("cargando menu", Fore.CYAN, 2), menu_opcion()),
     "chat": lambda:(circle_loader(), chatbot()),
    "terminal": lambda:(carga("cargando     terminal", Fore.BLUE, 2), commad())
    
    
  }
    return opcion
  
opcion = dict_menu()          








def UI_menu():
    
   #imprime el texto de menu
  print(Fore.YELLOW + txt)
  
  #Muestra el munu de opcio
  mostrar_mensaje(menum,Fore.CYAN)
  





def menu():
    
  UI_menu()
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
      
    elif player in clear:
      limpio()
      UI_menu()
    #ejecuta la funcion del diccionario 
    elif player in opcion:opcion[player]()#llama a la funcion correspondiente
    else:
      circle_loader()
        
      mostrar_mensaje("no es una opcion",Fore.RED)
      