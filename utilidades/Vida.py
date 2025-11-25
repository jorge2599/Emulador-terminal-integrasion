from utilidades.Verificar_Vida import validar
from colorama import init, Fore, Back
#Función de barra de vida


vida = validar()
def barra():
   porcentaje = vida / 10
   bloque = int(porcentaje * 10)
   if vida > 10 * 0.8:
     color = Fore.GREEN
   elif vida > 10 * 0.4:
     color = Fore.YELLOW
   else:
     color = Fore.RED
   barra = color + "█" * bloque + "" * (10 - bloque)
   return barra
   