# Emulador Terminal Integración

Proyecto personal donde integro todas mis prácticas y conocimientos de Python en un solo sistema modular.  
Incluye menú principal, chatbot interno, utilidades, juegos y un módulo matemático para resolver problemas usando fórmulas.

## 🚀 Objetivo del Proyecto

Reunir todas mis prácticas de Python en un solo sistema unificado, accesible desde un menú principal.  
El usuario puede navegar entre:

- Matemáticas (fórmulas, cálculos, herramientas)
- Chatbot asistente
- Juegos simples
- Utilidades visuales y de sistema
- Animaciones de carga
- Comandos personalizados
- Menús secundarios

Mi meta es que el programa evolucione hacia un asistente completo, capaz de:

- Guiar al usuario
- Ejecutar funciones específicas
- Registrar actividades
- Controlar módulos internos

## 📂 Estructura del Proyecto

```
Emulador-terminal-integrasion/
│
├── Matematicas/
│   ├── 
│   ├── 
│   ├── 
│   └── matematica.py
│
├── chatbot/
│   ├── Chat_bot.py
│   ├── Dialogo.json 
│   └── Bot_confing.py
│   
├── config/
│   ├── version.json
│   └── confing.py
│
├── interfas/
│   ├── menu-pricipal.py
│   └── menu_lista.py
│
├── juegos/
│   ├── Adivina_el_numero.py
│   └── Piedra_Papel_Tijera.py
│
├── utilidades/
│   ├── Carga.py
│   ├── Comando.py
│   ├── Cuadro.py
│   ├── Verificar_Vida.py
│   └── Vida.py
│
└── main.py
```

## 🧩 Módulos principales

### 🔹 1. Matemáticas

Ejercicios y fórmulas adaptadas para que el usuario resuelva problemas desde consola.

### 🔹 2. Chatbot

Asistente interno con:

- Respuestas básicas
- Animaciones de carga
- Mensajes personalizados

### 🔹 3. Interfaz (menú principal)

Sistema de navegación en consola que conecta todos los módulos.

### 🔹 4. Juegos

- Piedra, papel o tijera
- Adivina el número

### 🔹 5. Utilidades

Animaciones, cuadros, sistema de vida, verificación y comandos personalizados.

## 🔧 Instalación

Este proyecto solo utiliza la librería colorama para colores en la consola.  

Instalarla con:

```
pip install colorama
```

## ▶️ Ejecución

1. Clonar el repositorio:

```
git clone https://github.com/jorge2599/Emulador-terminal-integrasion
```

2. Entrar a la carpeta:

```
cd Emulador-terminal-integrasion
```

3. Ejecutar el programa:

```
python main.py
```

## 🛠️ Próximas mejoras

- Chatbot más inteligente con diálogo contextual
- Sistema de logs y registro
- Más juegos
- Módulos matemáticos avanzados
- Menú modular estilo “plugins”
- Limpieza y optimización del código

## 👤 Autor

Proyecto creado por Jorge Recalde como parte de su aprendizaje y práctica de Python
