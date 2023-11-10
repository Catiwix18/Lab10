from django.db import models
from django.http import JsonResponse

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

# Crear una vista para obtener la lista de productos en el formato requerido
def lista_productos(request):
    productos = Producto.objects.all()
    lista_productos_json = [
        {
            "codigo": producto.id,  # Cambia esto si quieres un campo diferente como el código.
            "descripcion": producto.nombre,
            "precio": float(producto.precio),
        }
        for producto in productos
    ]
    return JsonResponse(lista_productos_json, safe=False)
