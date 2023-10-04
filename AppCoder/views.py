from django.shortcuts import render, redirect
from AppCoder.models import Categoria, Producto, Pedido
from .forms import CategoriaForm, ProductoForm, PedidoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'AppCoder/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'AppCoder/crear_producto.html', {'form': form})

def buscar_productos(request):
    if request.method == 'POST':
        consulta = request.POST['consulta']
        productos = Producto.objects.filter(nombre__icontains=consulta)
    else:
        productos = Producto.objects.all()
    return render(request, 'AppCoder/buscar_productos.html', {'productos': productos})



