Filepath:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/blog/artículos.py
class Articulo:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def mostrar_articulo(self):
        print(f"--- {self.titulo} ---")
        print(self.contenido)
        print("--------------------")

# Example usage
articulo1 = Articulo("Importancia de la agricultura sostenible", "La agricultura sostenible es crucial para preservar el medio ambiente...")
articulo1.mostrar_articulo()

articulo2 = Articulo("Beneficios de la ganadería orgánica", "La ganadería orgánica promueve la salud de los animales y la calidad de los productos...")
articulo2.mostrar_articulo()
