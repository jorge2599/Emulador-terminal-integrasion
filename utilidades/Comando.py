import subprocess
from colorama import init, Fore
from utilidades.Carga import circle_animation as animation
from utilidades.Cuadro import mostrar_mensaje

def commad():
  while True:
    comando = input(Fore.CYAN + "==>")
    if comando == "salir":
       animation()
       break
    comando_ejecutable = subprocess.run(f"{comando}", shell=True, capture_output=True, text=True)
    salida = comando_ejecutable.stdout.strip() or "None"
    error = comando_ejecutable.stderr.strip() or "None"
    mostrar_mensaje("salida")
    print(Fore.GREEN + salida)
   
    mostrar_mensaje("error")
    print(Fore.RED + error)
  

