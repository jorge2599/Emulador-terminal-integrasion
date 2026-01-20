import random
from colorama import init, Fore, Back
from utilidades.Cuadro import mostrar_mensaje
from config.Juego_config.Confing_Juego import *






#función de adivina el numero
def adivinanum(vida):
    while True:
        mj = random.choice(res)
        mostrar_mensaje(mj, Fore.MAGENTA)
        intentos = 0
        IA = random.randint(1, 15)
        
        while True:
            if intentos == 5:
                mostrar_mensaje(f"Se acabó el límite. Hiciste {intentos} intentos", Fore.RED)
                break

            try:
                player = int(input(Fore.CYAN + "==> "))

                if player == 0:
                    mostrar_mensaje("Saliste del juego.", Fore.YELLOW)
                    return

                if player == IA:
                    mostrar_mensaje("¡Ganaste! 🎉", Fore.GREEN)
                    mostrar_mensaje("¿Quieres jugar de nuevo? (s/n)", Fore.YELLOW)
                    respuesta = input("=> ").lower()
                    if respuesta != "s":
                        mostrar_mensaje("Gracias por jugar 💖", Fore.MAGENTA)
                        return  # Sale de la función por completo
                    else:
                        break  # Sale del bucle interno, pero repite el juego completo

                elif player > IA:
                    chico = random.choice(chc)
                    intentos += 1
                    mostrar_mensaje(chico, Fore.CYAN)
                    continue

                elif player < IA:
                    grande = random.choice(gde)
                    intentos += 1
                    mostrar_mensaje(grande, Fore.CYAN)
                    continue

            except ValueError:
                intentos += 1
                mostrar_mensaje(random.choice(respuestas_invalidas), Fore.RED)
                continue
  
  
