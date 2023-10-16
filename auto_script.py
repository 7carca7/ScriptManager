"""Script Launcher"""

import os
import timeit
import logging

SCRIPTS_FOLDER = "Scripts/"


def setup_logging():
    """Defines registration system configuration"""

    logging.basicConfig(filename="reg.log", level=logging.INFO,
                        format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")


def get_python_scripts():
    """Get all the.py files inside the Scripts folder"""

    python_scripts = []

    for filename in os.listdir(SCRIPTS_FOLDER):
        if filename.endswith(".py"):
            python_scripts.append(filename)
    return python_scripts


scripts_to_run = get_python_scripts()
SCRIPTS_NUM = len(scripts_to_run)


def run_scripts():
    """Execute all the .py files inside the Scripts folder"""

    count = 1

    for script in scripts_to_run:
        print(f"EJECUTANDO {count}/{SCRIPTS_NUM} {script.upper()}")
        os.system(f"python3 {SCRIPTS_FOLDER}{script}")
        count += 1

    print(f"COMPLETADO {count - 1}/{SCRIPTS_NUM}")


setup_logging()

execution_time = timeit.timeit(run_scripts, number=1)
formatted_time = f"{execution_time:.2f}"

logging.info("TIEMPO(S)= %s", formatted_time)
print("TIEMPO(S)=", formatted_time)
