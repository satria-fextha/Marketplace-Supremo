class Usuario:
    def __init__(self, tipo, email, telefono, contraseña):
        self.tipo = tipo
        self.email = email
        self.telefono = telefono
        self.contraseña = contraseña
        self.verificado = False

    def registrar(self):
        # Lógica para registrar al usuario
        # Aquí se enviaría el correo o SMS de verificación
        self.verificado = True

    def acceder_perfil(self):
        # Lógica para acceder al perfil y funciones específicas según el tipo de usuario
        pass

class Agricultor(Usuario):
    def __init__(self, tipo, email, telefono, contraseña, productos, historia, certificaciones):
        super().__init__(tipo, email, telefono, contraseña)
        self.productos = productos
        self.historia = historia
        self.certificaciones = certificaciones

    def agregar_producto(self, producto):
        # Lógica para agregar un producto a la lista de productos del agricultor
        pass

    def editar_producto(self, producto):
        # Lógica para editar un producto existente del agricultor
        pass

class Ganadero(Usuario):
    def __init__(self, tipo, email, telefono, contraseña, productos, historia, certificaciones):
        super().__init__(tipo, email, telefono, contraseña)
        self.productos = productos
        self.historia = historia
        self.certificaciones = certificaciones

    def agregar_producto(self, producto):
        # Lógica para agregar un producto a la lista de productos del ganadero
        pass

    def editar_producto(self, producto):
        # Lógica para editar un producto existente del ganadero
        pass

class Consumidor(Usuario):
    def __init__(self, tipo, email, telefono, contraseña, historial_compras, preferencias, lista_deseos):
        super().__init__(tipo, email, telefono, contraseña)
        self.historial_compras = historial_compras
        self.preferencias = preferencias
        self.lista_deseos = lista_deseos

    def revisar_preferencias(self):
        # Lógica para revisar y ajustar las preferencias del consumidor
        pass

# Ejemplo de uso:
agricultor1 = Agricultor("agricultor", "agricultor1@example.com", "123456789", "contraseña123", [], "Historia del agricultor", [])
agricultor1.registrar()
agricultor1.acceder_perfil()
agricultor1.agregar_producto("Tomate")
agricultor1.editar_producto("Tomate")
