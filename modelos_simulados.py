# 🚗 Modelo simulado: Auto
# -------------------------------

class Auto:
    """Simula el comportamiento de un auto."""

    def __init__(self, marca: str):
        self.marca = marca
        self.velocidad = 0

    def acelerar(self, incremento: int):
        """Aumenta la velocidad del auto."""
        self.velocidad += incremento
        print(f"{self.marca} aceleró a {self.velocidad} km/h.")

    def frenar(self, decremento: int):
        """Reduce la velocidad del auto."""
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"{self.marca} frenó a {self.velocidad} km/h.")

    def estado(self):
        """Muestra el estado actual del auto."""
        print(f"{self.marca} está a {self.velocidad} km/h.")


# -------------------------------
# 🐟 Modelo simulado: Pez
# -------------------------------

class Pez:
    """Simula el comportamiento de un pez en movimiento."""

    def __init__(self, especie: str):
        self.especie = especie
        self.direccion = "norte"
        self.distancia = 0

    def nadar(self, metros: int):
        """El pez nada cierta distancia."""
        self.distancia += metros
        print(f"El {self.especie} nadó {metros} metros hacia el {self.direccion}.")

    def cambiar_direccion(self, nueva_direccion: str):
        """Cambia la dirección del pez."""
        self.direccion = nueva_direccion
        print(f"El {self.especie} cambió de dirección hacia el {self.direccion}.")

    def estado(self):
        """Muestra el estado actual del pez."""
        print(f"El {self.especie} ha nadado {self.distancia} metros hacia el {self.direccion}.")


# -------------------------------
#  Pruebas del proyecto
# -------------------------------

# Simulación de auto
auto1 = Auto("Toyota")
auto1.estado()
auto1.acelerar(50)
auto1.frenar(20)
auto1.estado()

# Simulación de pez
pez1 = Pez("salmón")
pez1.estado()
pez1.nadar(15)
pez1.cambiar_direccion("este")
pez1.nadar(10)
pez1.estado()
