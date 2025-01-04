print("Hola Git 3 V4")

# Diccionario de comandos útiles para GitHub

github_commands = {
    "gh repo create": "Crea un repositorio en GitHub desde la terminal.",
    "gh repo clone <url>": "Clona un repositorio desde GitHub.",
    "gh issue create": "Crea un nuevo issue en un repositorio.",
    "gh pr create": "Crea una pull request."
}

# Imprimir los comandos y sus descripciones
print("Comandos útiles para GitHub:")
for command, description in github_commands.items():
    print(f"  {command}: {description}")
