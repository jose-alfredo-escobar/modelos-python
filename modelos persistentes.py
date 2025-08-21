# 📘 Ejercicio 1: Guardar y leer una frase en un archivo

def guardar_frase():
    """Guarda una frase en un archivo de texto."""
    frase = "Estudiar todos los días mejora el aprendizaje."
    try:
        with open("frase.txt", "w", encoding="utf-8") as archivo:
            archivo.write(frase)
        print("Frase guardada correctamente.")
    except Exception as error:
        print(f"Error al guardar la frase: {error}")


def leer_frase():
    """Lee y muestra la frase guardada en el archivo."""
    try:
        with open("frase.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        print("Frase guardada:", contenido)
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as error:
        print(f"Error al leer la frase: {error}")


# 📗 Ejercicio 2: Guardar y leer una lista de tareas

def guardar_tareas():
    """Guarda una lista de tareas en un archivo."""
    tareas = [
        "Revisar apuntes de Python",
        "Practicar ejercicios de persistencia",
        "Subir proyecto a GitHub"
    ]
    try:
        with open("tareas.txt", "w", encoding="utf-8") as archivo:
            for tarea in tareas:
                archivo.write(tarea + "\n")
        print("Tareas guardadas correctamente.")
    except Exception as error:
        print(f"Error al guardar las tareas: {error}")


def leer_tareas():
    """Lee y muestra las tareas guardadas en el archivo."""
    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        print("Tareas pendientes:")
        for i, tarea in enumerate(lineas, start=1):
            print(f"{i}. {tarea.strip()}")
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as error:
        print(f"Error al leer las tareas: {error}")


# Bloque de pruebas
if __name__ == "__main__":
    guardar_frase()
    leer_frase()

    print("\n" + "=" * 40 + "\n")

    guardar_tareas()
    leer_tareas()
