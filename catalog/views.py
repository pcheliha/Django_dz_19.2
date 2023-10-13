from django.shortcuts import render

from catalog.models import Product, Category


def index(request):
    product = Product.objects.all()
    context = {'object_list': product}


    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contact.html')

def product(request, pk):
    product = Product.objects.filter(id=pk)
    context = {'object_list': product}
    return render(request, 'catalog/product.html', context)


def category(request):
    category = Category.objects.all()
    context = {'object_list': category}
    return render(request, 'catalog/category.html', context)
