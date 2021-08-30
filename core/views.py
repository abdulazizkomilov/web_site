from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

def checkout(request):
    return render(request, 'checkout.html')



# def product(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'product.html', context)


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'
