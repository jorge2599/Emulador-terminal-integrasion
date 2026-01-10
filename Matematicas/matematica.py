import random
from colorama import init, Fore, Back
from utilidades.Cuadro  import mostrar_mensaje
from utilidades.Carga import carga, circle_loader
from .Matematica_interes_compuesto import interes_compuesto
from .Menu_UI_matematica import UI_opcion
color = "\033[38;2;4;103;119m"
COLOR_MORADO = "\033[38;2;92;12;222m"




def menu_opcion():
    mostrar_mensaje(UI_opcion, COLOR_MORADO)
    while True:
      player = int(input("==>"))
      if player == 0:
       carga("regresando")
       break
      if player not in range(1,6):
       carga()
       mostrar_mensaje("uhh, ese numero como que no esta\nen la lista",Fore.GREEN)
       continue
     
      if player == 1:
       
       carga("cargado matematicas",Fore.YELLOW)
       matematicas
      elif player == 2:
       pass
   
      elif player == 3:
         circle_loader()
         interes_compuesto()
          
       
     
     
     
  #funcion de matematicas para operaciones básicas   
     
def matematicas():
  contador = 0
  mostrar_mensaje()
  while True:
    try:
    
       mate = int(input(f"{Fore.GREEN}==>"))
       if mate == 0:
         carga("Volviendo al menu de opciones",Fore.YELLOW)
         break
       if mate not in range(1,5):
         carga()
         mostrar_mensaje("coloca un numero\ncorrespondiente a la lista",Fore.RED)
       if mate == 1:
         carga()
         mostrar_mensaje("primer numero",Fore.YELLOW)
         num1 = int(input("==>"))
         carga()
         mostrar_mensaje("segundo numero",Fore.YELLOW)
         num2 = int(input("==>"))
         
         resultado = num1 + num2
         carga("sumando",Fore.YELLOW)
         mostrar_mensaje(f"la suma de {num1} y {num2}\nes {resultado}",Fore.GREEN)
         break
       
       elif mate ==2:
          carga()
          mostrar_mensaje("primer numero a restar",Fore.GREEN)
          resta = int(input(Fore.GREEN + "==>"))
          mostrar_mensaje("segundo numero",Fore.YELLOW)
          Resta = int(input(Fore.GREEN + "==>"))
          resta -= Resta
          mostrar_mensaje(f"el resultado es {resta}")
          
          
       elif mate ==3:
          carga()
          mostrar_mensaje("primer numero a multiplicar",Fore.GREEN)
          multiplicar = int(input(Fore.GREEN + "==>"))
          mostrar_mensaje("segundo numero s Multiplicar",Fore.YELLOW)
          Multiplicar = int(input(Fore.GREEN + "==>"))
          multiplicar *= Multiplicar
          carga("calculando")
          mostrar_mensaje(f"el resultado es {multiplicar}")
          
          
       elif mate == 4:
          carga()
          mostrar_mensaje("primer numero a dividir",Fore.GREEN)
          dividir = int(input(Fore.GREEN + "==>"))
          mostrar_mensaje("segundo numeroa dividir",Fore.YELLOW)
          Dividir = int(input(Fore.GREEN + "==>"))
          dividir /= Dividir
          mostrar_mensaje(f"el resultado es {dividir}")
          
        
    except ValueError:
       mostrar_mensaje("para mi que tienes que\ncolocar un numero:)")

#funcion para saber o calcular el diametro
def diametro():
  mostrar_mensaje("")

