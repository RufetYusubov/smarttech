from django.shortcuts import render, HttpResponse
from  ultracomp.models import LaptopModel


def laptop(request):
    laptops = LaptopModel.objects.order_by("price")
    context = {
        "laptops" : laptops,
    }
    return render(request, 'laptop.html', context)

def details(request,id):
    laptop = LaptopModel.objects.get(id=id)

    context = {
        "laptop" : laptop
    }
    return render(request, 'details.html', context)