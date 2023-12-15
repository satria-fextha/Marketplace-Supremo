Explicación:

Este archivo de Python define dos modelos Django para representar categorías y productos en una aplicación de comercio electrónico de productos agrícolas y ganaderos.

Clase Categoria:

Esta clase representa una categoría de productos. Cada categoría tiene un nombre único que se almacena en el campo nombre.

Clase Producto:

Esta clase representa un producto individual. Cada producto tiene los siguientes campos:

nombre: El nombre del producto.
descripcion: Una descripción detallada del producto.
precio: El precio del producto en formato decimal.
imagen: La imagen del producto.
categoria: La categoría a la que pertenece el producto. Esta relación se establece mediante una clave externa a la clase Categoria.
Uso:

Estos modelos se utilizan para almacenar información sobre categorías y productos en una base de datos relacional. La aplicación de comercio electrónico puede utilizar esta información para mostrar una lista de productos en categorías específicas, buscar productos por nombre o categoría, y agregar productos al carrito de compras de un usuario.

Ruta:

El archivo Python se encuentra en la siguiente ruta:

Funcionalidades/Products/models.py
Esta ruta indica que el archivo se encuentra en la carpeta Funcionalidades/Products dentro del proyecto.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
