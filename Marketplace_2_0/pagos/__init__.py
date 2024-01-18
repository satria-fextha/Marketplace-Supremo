class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def resumen_carro(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return f"Total a pagar: {total}"

class Pedido:
    def __init__(self, vendedor, consumidor):
        self.vendedor = vendedor
        self.consumidor = consumidor
        self.estado = "En proceso"

    def aceptar_pedido(self):
        self.estado = "Aceptado"
        self.consumidor.notificar_estado(self.estado)

    def rechazar_pedido(self):
        self.estado = "Rechazado"
        self.consumidor.notificar_estado(self.estado)

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.consumidor.notificar_estado(self.estado)

class Vendedor:
    def __init__(self):
        self.pedidos = []

    def gestionar_pedido(self, pedido, accion):
        if accion == "aceptar":
            pedido.aceptar_pedido()
        elif accion == "rechazar":
            pedido.rechazar_pedido()
        elif accion == "actualizar":
            nuevo_estado = input("Ingrese el nuevo estado del pedido: ")
            pedido.actualizar_estado(nuevo_estado)

class Consumidor:
    def __init__(self):
        self.pedidos = []

    def notificar_estado(self, estado):
        print(f"El estado de su pedido ha sido actualizado: {estado}")

# Ejemplo de uso
carro = CarroDeCompras()
carro.agregar_producto(Producto("Producto 1", 10))
carro.agregar_producto(Producto("Producto 2", 20))
print(carro.resumen_carro())

vendedor = Vendedor()
consumidor = Consumidor()
pedido = Pedido(vendedor, consumidor)
vendedor.gestionar_pedido(pedido, "aceptar")
