print("new Hola Git")
# Diccionario de comandos de Git y su descripción

git_commands = {
    "Comandos básicos de Git": {
        "git init": "Inicializa un nuevo repositorio Git en el directorio actual.",
        "git clone <url>": "Clona un repositorio remoto a tu máquina local.",
        "git add <archivo>": "Agrega un archivo al área de preparación (staging).",
        "git add .": "Agrega todos los archivos en el directorio actual al área de preparación.",
        "git commit -m 'mensaje'": "Crea un commit con un mensaje descriptivo.",
        "git status": "Muestra el estado actual del repositorio (archivos modificados, preparados, etc.).",
        "git log": "Muestra el historial de commits.",
        "git branch": "Lista las ramas actuales.",
        "git branch <nombre>": "Crea una nueva rama con el nombre especificado.",
        "git checkout <rama>": "Cambia a la rama especificada.",
        "git merge <rama>": "Fusiona la rama especificada con la rama actual.",
        "git pull": "Descarga y fusiona los cambios desde el repositorio remoto.",
        "git push": "Sube los cambios al repositorio remoto.",
        "git remote add origin <url>": "Conecta el repositorio local con un remoto.",
        "git diff": "Muestra los cambios no comprometidos."
    }

   
}

# Imprimir los comandos organizados
for section, commands in git_commands.items():
    print(f"{section}:")

    for command, description in commands.items():
        print(f"  {command}: {description}")
    print()
