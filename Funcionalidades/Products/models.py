Funcionalidades/Products/models.py
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


class Agricultor(models.Model):
    nombre = models.CharField(max_length=50)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre


class Consumidor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Busqueda(models.Model):
    nombre_producto = models.CharField(max_length=50)
    tipo_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_minimo = models.DecimalField(max_digits=8, decimal_places=2)
    precio_maximo = models.DecimalField(max_digits=8, decimal_places=2)
    ubicacion_vendedor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_producto
