from colorama import init, Fore, Back


init(autoreset=True)
#Función para mostrar texto con marco y color

def mostrar_mensaje(texto, color=Fore.WHITE):
    lineas = texto.split("\n")
    largo = max(len(linea) for linea in lineas)
    print(color + "╔" + "═" * (largo + 2) + "╗")
    for linea in lineas:
        print(color + "║ " + linea.ljust(largo) + " ║")
    print(color + "╚" + "═" * (largo + 2) + "╝")