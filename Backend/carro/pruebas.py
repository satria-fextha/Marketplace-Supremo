class CarroDeCompras:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def actualizar_cantidad(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] = cantidad

    def eliminar_producto(self, producto):
        if producto in self.productos:
            del self.productos[producto]

# Pruebas
carro = CarroDeCompras()
carro.agregar_producto("Producto 1", 2)
carro.agregar_producto("Producto 2", 3)
carro.actualizar_cantidad("Producto 1", 5)
carro.eliminar_producto("Producto 2")
print(carro.productos)
