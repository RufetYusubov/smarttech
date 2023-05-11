from django.shortcuts import render, HttpResponse
from  ultracomp.models import LaptopModel


def laptop(request):
    laptops = LaptopModel.objects.order_by("brend")
    context = {
        "laptops" : laptops,
    }
    return render(request, 'laptop.html', context)