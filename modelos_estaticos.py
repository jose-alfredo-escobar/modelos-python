class Usuario:
    """Modelo estático para representar un usuario."""

    def __init__(self, nombre: str, edad: int, correo: str):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo


# -------------------------------
# Modelo estático de Producto
# -------------------------------

class Producto:
    """Modelo estático para representar un producto."""

    def __init__(self, nombre: str, precio: float, categoria: str):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


# -------------------------------
# Pruebas del modelo
# -------------------------------

# Crear instancia de Usuario
usuario1 = Usuario("Ana", 28, "ana@example.com")

print("Información del usuario:")
print(f"Nombre: {usuario1.nombre}")
print(f"Edad: {usuario1.edad}")
print(f"Correo: {usuario1.correo}")

# Crear instancia de Producto
producto1 = Producto("Laptop", 1200.00, "Electrónica")

print("\nInformación del producto:")
print(f"Nombre: {producto1.nombre}")
print(f"Precio: ${producto1.precio:.2f}")
print(f"Categoría: {producto1.categoria}")
