"Script que ejecutarán todos los comandos de brew"

import os

commands = [
    "brew update",
    "brew upgrade",
    "brew autoremove",
    "brew cleanup --prune=0 -s"
]

for cmd in commands:
    try:
        print(f"Ejecutando comando: {cmd}")
        os.system(cmd)

    except ImportError as error:
        print(f"Error: {error}")
