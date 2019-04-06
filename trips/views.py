from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def trip_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "trips/trip_create.html", context)


def trip_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.desc
    # }
    context = {
        'object': obj
    }
    return render(request, 'trips/detail.html', context)
