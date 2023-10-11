from django.shortcuts import render
from productos.models import Producto  
from django.template import loader

def index(request):
    data = {
        "foto" : "logo.jpg",
    }
    return render (request, 'web/index.html', context=data)
  
    

def user(request):
    return render(request, 'web/user.html')

def productos(request):
    productos = Producto.objects.all()

    # Diccionario de contexto
    data = {
        "titulo": "Productos",
        "categorias": ["Categoría 1", "Categoría 2", "Categoría 3"],
        "productos": productos,
    }
    return render(request, 'web/productos.html', data)


    
def computacion(request):
    productos_computacion = Producto.objects.filter(categorias="Computacion")
    
    data = {
        "titulo":"Computacion",
        "subtitulo":"Aquí encontrarás los mejores precios en Computacion.",
        "categorias":["Computacion","Consolas y Videojuegos"] ,
        "foto1" : "computacion1.jpg",
        "foto2" : "computacion2.jpg",
        "foto3" : "computacion3.jpg",
        
        "productos":productos_computacion,
    }

    return render(request, 'web/computacion.html', data)

def consola(request):
    productos_consola = Producto.objects.filter(categorias="Consolas")

    data = {
        "titulo":"Consolas",
        "subtitulo": "Descubre nuestra selección de consolas de videojuegos.",
        "categorias":["Computacion","Consolas y Videojuegos"] ,
        "foto1" : "consolas1.jpg",
        "foto2" : "consolas2.jpg",
        "foto3" : "consolas3.jpg",

        "productos":productos_consola,
    }

    return render(request, 'web/consolas.html', data)

def videojuegos(request):
    productos_videojuegos = Producto.objects.filter(categorias="Videojuegos")

    data = {
        "titulo":"Videojuegos",
        "subtitulo":"Disfruta de nuestros juegos favoritos",
        "categorias":["Computacion","Consolas y Videojuegos"] ,
        "foto1" : "videojuegos1.jpg",
        "foto2" : "videojuegos2.jpg",
        "foto3" : "videojuegos3.jpg",
        "productos":productos_videojuegos,
    }
    
    return render(request, 'web/videojuegos.html', data)
