from colorama import init, Fore, Back
import random
from utilidades.Cuadro import mostrar_mensaje
from utilidades.Carga import carga
import os

#borra la terminal
os.system('cls' if os.name == 'nt' else 'clear')



#mensaje de inicio
mg =["Ingresa un numero de 1 al 10","por favor Ingresa un numero del\n1 al 10 no menos\nde 0 no superios a 10"]
#mensaje de menor a 0
mn =["acaso no leiste el mensaje\ndel inicio","Que parte de no se admite\nlos numeros negativos\nno entendiste"]
#mensaje de mayor a 10
mayor_10 = [
    "¿Más de 10? Qué ambicioso... \n¿También querés conquistar Marte con eso?",
    "¡Alguien apunta alto! \nLástima que el juego no.",
    "¿10 no era suficiente? \n¿Querés romper el sistema \no solo aburrirme?",
    "Pensé que sabías contar hasta 10, \npero veo que sos un visionario.",
    "Eso es más de 10... \n¿Querés que el universo colapse \no solo estás probando mi paciencia?"
]
#mensaje de un caracter
mensajes_caracter = [
    "¿Una letra?\nClaro, el alfabeto también quiere jugar, ¿no?",
    "¡Perfecto!\nJusto lo que esperaba… menos un número.",
    "¿Un carácter?\nMe hiciste reír. Pero no, eso no sirve.",
    "¡Ah, sí!\nPorque claramente 'banana' es un número...",
    "Excelente jugada, campeón.\nPero los números no tienen letras (todavía)."
]




#Entrada de vida
carga("cargando programa", Fore.CYAN, 2)
def validar():
  vie = random.choice(mg)
  mostrar_mensaje(vie,Fore.CYAN)
  while True:
    try:
      player = int(input(Fore.GREEN + "==>"))
      if player <=0:
        m = random.choice(mn)
        mostrar_mensaje(m, Fore.RED)
        continue
      if player <= 10:
        return player
      else:
        mayor = random.choice(mayor_10)
        mostrar_mensaje(mayor, Fore.YELLOW)
        continue
    except ValueError:
      cr = random.choice(mensajes_caracter)
      mostrar_mensaje(cr,Fore.RED)
      continue
if __name__ == "__main__":
     vida = validar()
