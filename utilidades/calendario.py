import datetime
   
   
   
hoy = datetime.datetime.now()

#diccionario de los meses 
mes = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

#lista de la semana 
semana = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]

#funcion para octener semana 
def fecha_semana():
    return semana[hoy.weekday()]


#Funcion para obtener mes   
def fecha_mes():
    return mes[hoy.month]

#Funcion de hora
def tiempo_Hora():
    return hoy.hour
    
#funcion de minutos 
def tiempo_minuto():
    return hoy.minute


#funcion de segundos
def tiempo_segundo():
    return  hoy.second
    