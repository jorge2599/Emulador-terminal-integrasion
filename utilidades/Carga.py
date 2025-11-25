from colorama import init, Fore, Back
import sys
import time
import itertools

#Función de carga 
def carga(carga="cargando",color=Fore.GREEN, Lee = 3):
  for _ in range(Lee):
    for i in [".","..","..."]:
      #borra los puntos
      sys.stdout.write("\r" + " " * (len(carga) + 5) + "\r")
      sys.stdout.write( "\r"+ f"{color}{carga}{i}")
      sys.stdout.flush()
      time.sleep(0.5)
  #borra el final
  sys.stdout.write("\r" + " " * 30 + "\r")
  sys.stdout.flush()
  


def circle_animation(repeticiones=3, color=Fore.LIGHTMAGENTA_EX):
      positions = [
        "⡀", "⡁", "⡂", "⡃", "⡄", "⡅", "⡆", "⡇",
        "⡏", "⡟", "⡿", "⣿", "⣾", "⣽", "⣻", "⢿"
     ]
      i = 0
      while True:
        sys.stdout.write('\r' + positions[i])
        sys.stdout.flush()
        i = (i + 1) % len(positions)
        time.sleep(0.1)
         # Controla las repeticiones
         # Cada vez que el índice vuelve a 0, se ha completado una vuelta
        if i == 0:
          repeticiones -= 1
          if repeticiones == 0:
            sys.stdout.write('\r' + ' ' * 2 + '\r')  # Limpia el símbolo al final
            sys.stdout.flush()
            break

# Secuencia de caracteres para el círculo animado
circle_chars = ['◜', '◜◝', '◟◞']


def circle_loader():
    repetitions = 10 # Número de repeticiones del ciclo
     # Ciclo infinito para la animación
    for char in itertools.cycle(circle_chars):
        sys.stdout.write('\r'+ Fore.LIGHTRED_EX + char)
        sys.stdout.flush()
        time.sleep(0.1)
        # Controla las repeticiones
        if repetitions <= 0:
            sys.stdout.write('\r' + ' ' * len(char) + '\r')  # Limpia el símbolo al final
            sys.stdout.flush()
            break
        if char == circle_chars[-1]:
            repetitions -= 1
            
       