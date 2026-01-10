import sys, time
from colorama import Fore


def efecto_maquina_de_escribir(msj,color=Fore.CYAN):
       for char in msj:
           sys.stdout.write(color + char)
           sys.stdout.flush()
           time.sleep(0.05)
       print()
