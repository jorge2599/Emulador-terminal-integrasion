import random
from colorama import init, Fore, Back
from utilidades.Cuadro import mostrar_mensaje


#respuestas para aduvida el numero

res = [
    "Vamos a jugar un poco 🎲\nElige un número del 1 al 15\npara intentar adivinar el mío.\n(0 para salir si te rendís)",

    "Hmm... ¿en qué número crees\nque estoy pensando?🤔\nProbá del 1 al 15.\n(0 para salir jeje)",

    "Estoy pensando en un número secreto...😏\n¿Te animás a adivinar?\nDel 1 al 15.\n(0 si te da miedo perder)",

    "No todos los días podés leer\nla mente de una IA misteriosa 👁️\nIntentalo. Del 1 al 15.\n(0 para abandonar el juego)",


    "Tu destino depende de un número🎯\nElegí del 1 al 15 si te animás...\nO escapá con un 0, cobarde😜",

    "¿Querés jugar conmigo? 😈\nElegí un número entre 1 y 15...\nO poné 0 si ya estás temblando.",

    "No voy a decir que tengo poderes\npsíquicos, pero casi...\nProbá del 1 al 15.\n(0 si te rendiste antes de empezar)",

    "¡El oráculo digital ha hablado! 😌\nEstoy pensando un número...\n¿Del 1 al 15? (0 para escapar)",

    "Vamos, elegí un número serio.\nDel 1 al 15.\n(0 para salir si te dio cagazo)",

    "¿Número mágico o maldito? 🎩✨\nAdiviná del 1 al 15...\n(0 para abandonar esta dimensión)",

    "Solo un número entre 1 y 15.\n¿Tan difícil puede ser? 😏\n(0 si te da vértigo jugar conmigo)",

    "¿Otra vez querés jugar?\nDel 1 al 15 tenés tus chances.\n(0 si ya te cansaste de perder)"
]

gde = [
    "Es más grande el número\nen el que estoy pensando.",
    "Para mí que es más grande\nel número en mi procesador, jaja.",
    "Mmm... subí un poco,\nese número está muy bajo.",
    "Nope. Vas corto,\ntiene que ser más alto 😉."
]
chc = [
    "Uhh, para mí que tenés\nque pensar en un número más chico.",
    "Che, según mi procesador,\nes más chico jaja.",
    "Bajá un poco, ese número\ntiene hambre de humildad.",
    "Demasiado alto.\nIntentá con uno más chiquito 🐭."
]

respuestas_invalidas = [
    "Eso no es un número...\nPero tampoco vos sos un aporte positivo a la sociedad.\nCoincidencias, ¿no?",
    "Entrada inválida.\nComo tu presencia en la vida de tu padre.\nUps, lo dije.",
    "¿Eso era un número?\nPensé que era tu coeficiente\nintelectual disfrazado.\nFalló igual.",
    "No, eso no es un número.\nEs tu trauma infantil escribiendo desde el subconsciente.\nOtra vez.",
    "Error de input.\nAsí como ese número es inválido,\ntu vida amorosa también lo es.",
    "Ni la IA quiso procesarlo.\nY esta IA responde hasta a teorías conspiranoicas.\nAsí de mal estamos.",
    "Eso tiene menos lógica que tus decisiones un domingo a las 3 AM.\n\nY duele igual.",
    "Eso no es un número.\nEs un grito de ayuda con mala ortografía.\nTe leímos.",
    "Valor inválido.\nComo tu existencia en los planes de Dios.\nFuerte, pero cierto.",
    "Tu número fue rechazado.\nComo tu solicitud de afecto en la infancia.\nSeguimos sumando traumas.",
    "Eso no es un número.\nEs una señal del universo para que apagues todo\nY vayas a llorar al baño.",
    "¿Qué fue eso?\nNi Cthulhu entiende esa entrada.\nY él ha visto cosas."
]


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
  
  
