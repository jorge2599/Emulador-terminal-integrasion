from utilidades.Cuadro import mostrar_mensaje

from colorama import Fore, init

init(autoreset=True)

def interes_compuesto():
    try:
        mostrar_mensaje("Ingresa tu capital inicial" ,Fore.GREEN)
        capital = int(input(Fore.CYAN + "==>"))
        
        mostrar_mensaje("Ingresa tu tasa de interes anual")
        tasa = float(input(Fore.CYAN + "==>"))
        mostrar_mensaje("Ingresa el tiempo que invertiras en años", Fore.BLUE)
        tiempo = int(input(Fore.CYAN + "==>"))
        
        mostrar_mensaje("Ingresa la capitalizacion",Fore.CYAN)
        capitalizaciones= int(input(Fore.CYAN + "==>"))
        
    except ValueError:
        mostrar_mensaje("Verifica que los datos\ningresados sean correctos",Fore.RED)
    
    resultado = capital * (1 + tasa / capitalizaciones) ** (capitalizaciones * tiempo)
    
    mostrar_mensaje(f"Monto final: ${resultado:.2f}")
    


