"Lanzador de scripts"

import os
import timeit
import datetime

scripts_folder = os.path.join(os.getcwd(), "Scripts", "")


def timestamp_log():
    "Crea un archivo txt con el timestamp actual"

    hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    directorio = os.getcwd()
    ruta_archivo = os.path.join(directorio, "log.txt")

    contenido_anterior = ""
    contenido_nuevo = f"{hora_actual} - EJECUTADO EN {execution_time:.2f} SEGUNDOS.\n"

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding="utf-8") as archivo:
            contenido_anterior = archivo.read()

    contenido_total = contenido_nuevo + contenido_anterior

    with open(ruta_archivo, 'w', encoding="utf-8") as archivo:
        archivo.write(contenido_total)


def get_python_scripts():
    "Obtiene todos los archivos.py dentro del directorio Scripts"

    python_scripts = []

    for filename in os.listdir(scripts_folder):
        if filename.endswith(".py"):
            python_scripts.append(filename)
    return python_scripts


scripts_to_run = get_python_scripts()
SCRIPTS_NUM = len(get_python_scripts())


def run_scripts():
    "Ejecuta todos los archivos.py dentro del directorio Scripts"

    count = 1

    for script in scripts_to_run:
        print(f"EJECUTANDO {count}/{SCRIPTS_NUM} {script.upper()}")
        os.system(f"python3 {scripts_folder}{script}")
        count += 1

    print(f"COMPLETADO {count - 1}/{SCRIPTS_NUM}")


execution_time = timeit.timeit(run_scripts, number=1)
print(f"DURACIÓN {execution_time:.2f} SEGUNDOS")
timestamp_log()
