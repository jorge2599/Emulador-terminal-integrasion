# Emulador Terminal Integrasion

este es mi proyecto donde meto todo lo que voy aprendiendo de python  
arrancó como un script simple con piedra papel tijera y vidas este proyecto va evolucionando a medida que aprendo

es una terminal con menú, juegos, matemáticas, un chatbot que todavía estoy armando y tambien es una asistente que te ayuda y proporciona informacion del proyecto ("Bueno eso estoy queriendo que haga jeje:)")

## capturas para que veas cómo se ve

### pantalla de carga
<p align="center">
  <img src="assets/inicio.png" alt="pantalla de carga" width="500">
</p>

### elección de vida
<p align="center">
  <img src="assets/vida.png" alt="elección de vida" width="500">
</p>

### menú principal
<p align="center">
  <img src="assets/Menu.png" alt="menú principal" width="500">
</p>

## qué tiene ahora
- menú con comandos: salir, vida (tu estado), juego (juegos), opcion (funciones), chat, borra (limpia pantalla), terminal (abre otra consola)
- vida que se guarda y tiene barra visual
- juegos: adivina el número, piedra papel tijera
- matemáticas: cálculo simple, diámetro, interés compuesto...
- chatbot básico (responde saludos y cosas simples)
- config  (version.json)
- validaciones cuando te equivocás (mensajes claros)
- animaciones de carga y cuadros con color

## cómo correrlo
1. cloná el repo  
   git clone https://github.com/jorge2599/Emulador-terminal-integrasion.git  
   cd Emulador-terminal-integrasion

2. instalá colorama (lo único que necesita)  
   pip install colorama

3. dale play  
   python main.py

## estructura de carpetas
```
Emulador-terminal-integrasion/
│
├── Matematicas/
│   ├── Matematica_ interes_compuesto.py
│   ├── Matematica_calculo_simple.py
│   ├── Matematica_diametro.py
│   ├── matematica.py
│   └── Menu_UI_matematica.py
│
│
│
├── assets/
│   ├── inicio.png
│   ├── vida.png
│   └── Menu.png
│
│               
├── chatbot/
│   ├── animaciones_del_bot/
│   │   ├──animacion_escritura_bot.py
│   │      
│   ├── Chat_bot.py
│   ├── Dialogo.json 
│   └── Bot_confing.py
│   
├── config/
│   ├── version.json
│   └── confing.py
│
├── UI/
│   ├── confing_ui/
│   │     ├── UI_Chatbot.py
│   │     ├── UI_Juegos.py
│   │     ├── UI_lista.py
│   │     ├── UI_mate.py
│   │     └── UI_utils.py
│   ├── UI_pricipal.py
│   └── Clave_dato_comando.py
│
├── juegos/
│   ├── Adivina_el_numero.py
│   └── Piedra_Papel_Tijera.py
│
├── utilidades/
│   ├── calendario.py
│   ├── limpia_terminal.py
│   ├── Carga.py
│   ├── Comando.py
│   ├── Cuadro.py
│   ├── Verificar_Vida.py
│   └── Vida.py
│
│
├── LICENSE
│
│
├── README.MD
│
│
└── main.py
```

## Nuevas mejoras
He implementado nuevas mejoras en el código. Optimicé los imports de la UI principal y agregué nuevos paquetes y módulos, asignando a cada uno una única responsabilidad.
En el paquete de matemática, incorporé un nuevo módulo que se encarga exclusivamente de gestionar los menús matemáticos.
En utilidades, añadí un módulo de fecha cuya función es organizar y registrar el orden, la fecha y la hora de ejecución de cada parte del proyecto.
Además, creé un paquete específico para las animaciones del bot, destinado a contener únicamente las animaciones exclusivas del chatbot.


## próximas cosas que  voy a hacer o mejorar y agregrar 
- mejorar el chat con más respuestas y lógica
- Agregar un registro de usuario
- menu de informacion basica segun el inicio de sesion
- nuevas animaciones
- agregar logs de lo que hacés
- quizás un descargador de yt
- más juegos y y funciones
- algún día probar pygame
- 

es mi lugar para practicar, así que va cambiando cada vez que aprendo algo nuevo.