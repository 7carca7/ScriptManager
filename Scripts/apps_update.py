"Script que buscará e instalará actualizaciones de apps y del systema"

import os

commands = [
    # "brew update",
    # "brew upgrade",
    # "brew autoremove",
    # "brew cleanup",
    # "mas upgrade",
    # "softwareupdate -ia --verbose",

]

for cmd in commands:
    try:
        print(f"Ejecutando comando: {cmd}")
        os.system(cmd)

    except ImportError as error:
        print(f"Error: {error}")
