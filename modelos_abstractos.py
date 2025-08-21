from abc import ABC, abstractmethod
import math

# -------------------------------
# Ejercicio 1: Figuras geométricas
# -------------------------------

class Figura(ABC):
    """Modelo abstracto para figuras geométricas."""

    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura."""
        pass


class Rectangulo(Figura):
    """Representa un rectángulo con base y altura."""

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura


class Circulo(Figura):
    """Representa un círculo con radio."""

    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)


# Prueba de figuras
rect = Rectangulo(4, 5)
circ = Circulo(3)

print("Áreas de figuras geométricas:")
print(f"Rectángulo: {rect.calcular_area():.2f}")
print(f"Círculo: {circ.calcular_area():.2f}")

# -------------------------------
# Ejercicio 2: Métodos de pago
# -------------------------------

class MetodoPago(ABC):
    """Modelo abstracto para métodos de pago."""

    @abstractmethod
    def procesar_pago(self, monto: float):
        """Procesa el pago por el monto indicado."""
        pass


class PagoTarjeta(MetodoPago):
    """Procesa pagos con tarjeta."""

    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto:.2f} con tarjeta...")


class PagoEfectivo(MetodoPago):
    """Procesa pagos en efectivo."""

    def procesar_pago(self, monto: float):
        print(f"Procesando pago de ${monto:.2f} en efectivo...")


# Prueba de pagos
tarjeta = PagoTarjeta()
efectivo = PagoEfectivo()

print("\nProcesamiento de pagos:")
tarjeta.procesar_pago(150.75)
efectivo.procesar_pago(80.00)
