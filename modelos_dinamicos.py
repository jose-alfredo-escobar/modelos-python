# -------------------------------
# 🏦 Modelo dinámico: Cuenta Bancaria
# -------------------------------

class CuentaBancaria:
    """Representa una cuenta bancaria con operaciones básicas."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto: float):
        """Agrega dinero a la cuenta."""
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso: ${monto:.2f}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto: float):
        """Retira dinero si hay suficiente saldo."""
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso: ${monto:.2f}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        """Muestra el saldo actual."""
        print(f"Saldo actual de {self.titular}: ${self.saldo:.2f}")


# -------------------------------
#  Modelo dinámico: Inventario
# -------------------------------

class Inventario:
    """Representa un inventario de productos."""

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre: str, cantidad: int):
        """Agrega productos al inventario."""
        if cantidad > 0:
            if nombre in self.productos:
                self.productos[nombre] += cantidad
            else:
                self.productos[nombre] = cantidad
            print(f"Se agregaron {cantidad} unidades de '{nombre}'.")
        else:
            print("La cantidad debe ser positiva.")

    def vender_producto(self, nombre: str, cantidad: int):
        """Vende productos si hay suficiente stock."""
        if nombre in self.productos and self.productos[nombre] >= cantidad:
            self.productos[nombre] -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de '{nombre}'.")
        else:
            print("Stock insuficiente o producto no disponible.")

    def mostrar_inventario(self):
        """Muestra el inventario actual."""
        print("\n Inventario actual:")
        for nombre, cantidad in self.productos.items():
            print(f"- {nombre}: {cantidad} unidades")


# -------------------------------
#  Pruebas del proyecto
# -------------------------------

# Cuenta bancaria
cuenta = CuentaBancaria("José", 100.0)
cuenta.mostrar_saldo()
cuenta.depositar(50.0)
cuenta.retirar(30.0)
cuenta.retirar(150.0)
cuenta.mostrar_saldo()

# Inventario
inventario = Inventario()
inventario.agregar_producto("Laptop", 10)
inventario.agregar_producto("Mouse", 25)
inventario.vender_producto("Laptop", 3)
inventario.vender_producto("Teclado", 1)
inventario.mostrar_inventario()
