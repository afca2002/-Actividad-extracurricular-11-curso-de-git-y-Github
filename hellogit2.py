print("Hola Git2")
# Diccionario de comandos de Git y su descripción

git_commands = {
   
    "Comandos avanzados de Git": {
        "git stash": "Guarda temporalmente los cambios no confirmados.",
        "git stash apply": "Recupera los cambios guardados en el stash.",
        "git reset <archivo>": "Elimina un archivo del área de preparación.",
        "git reset --hard": "Revierte el repositorio al último commit (¡Cuidado, es irreversible!).",
        "git rebase <rama>": "Aplica los cambios de otra rama sobre la rama actual."
    }
}

# Imprimir los comandos organizados
for section, commands in git_commands.items():
    print(f"{section}:")
    
    for command, description in commands.items():
        print(f"  {command}: {description}")
    print()
