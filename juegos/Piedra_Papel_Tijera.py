import random
from colorama import init, Fore, Back
from utilidades.Cuadro import mostrar_mensaje



#función de piedra_papel_tijera
def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    mostrar_mensaje("¡Piedra, papel o tijera!\nEscribe tu elección o 'salir' para volver.", Fore.MAGENTA)

    while True:
        player = input(Fore.CYAN + "==> ").lower()
        if player == "salir":
            mostrar_mensaje("Volviendo al menú principal...", Fore.YELLOW)
            break
        if player not in opciones:
            mostrar_mensaje("Esa no es una opción válida.\nUsá: piedra, papel o tijera.", Fore.RED)
            continue

        IA = random.choice(opciones)
        mostrar_mensaje(f"La IA eligió: {IA}", Fore.BLUE)

        if player == IA:
            mostrar_mensaje("¡Empate! 🤝", Fore.CYAN)
        elif (
            (player == "piedra" and IA == "tijera") or
            (player == "papel" and IA == "piedra") or
            (player == "tijera" and IA == "papel")
        ):
            mostrar_mensaje("¡Ganaste esta ronda! 🎉", Fore.GREEN)
        else:
            mostrar_mensaje("Perdiste... 😢", Fore.RED)

        mostrar_mensaje("¿Otra ronda? (s/n)", Fore.YELLOW)
        respuesta = input("=> ").lower()
        if respuesta != "s":
            mostrar_mensaje("Gracias por jugar ✨", Fore.MAGENTA)
            break
          
          
          
          