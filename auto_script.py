"Lanzador de scripts"

import os
import timeit
import logging

SCRIPTS_FOLDER = "Scripts/"


def setup_logging():
    "Define la configuración del sistema de registro"

    logging.basicConfig(filename="reg.log", level=logging.INFO,
                        format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")


def get_python_scripts():
    "Obtiene todos los archivos.py dentro del directorio Scripts"

    python_scripts = []

    for filename in os.listdir(SCRIPTS_FOLDER):
        if filename.endswith(".py"):
            python_scripts.append(filename)
    return python_scripts


scripts_to_run = get_python_scripts()
SCRIPTS_NUM = len(scripts_to_run)


def run_scripts():
    "Ejecuta todos los archivos.py dentro del directorio Scripts"

    count = 1

    for script in scripts_to_run:
        print(f"EJECUTANDO {count}/{SCRIPTS_NUM} {script.upper()}")
        os.system(f"python3 {SCRIPTS_FOLDER}{script}")
        count += 1

    print(f"COMPLETADO {count - 1}/{SCRIPTS_NUM}")


setup_logging()

execution_time = timeit.timeit(run_scripts, number=1)
formated_time = f"{execution_time:.2f}"

logging.info("TIEMPO(S)= %s", formated_time)
print("TIEMPO(S)=", formated_time)
