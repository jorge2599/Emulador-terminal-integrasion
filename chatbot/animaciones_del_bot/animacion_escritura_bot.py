import sys, time
from colorama import Fore, Style

def efecto_maquina_de_escribir(msj, color=Fore.WHITE):
    for char in msj:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.05)

    sys.stdout.write(Style.RESET_ALL + "\n")
    sys.stdout.flush()
