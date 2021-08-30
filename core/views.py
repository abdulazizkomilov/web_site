from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Item


class CheckoutPegeView(TemplateView):
    template_name = 'checkout-page.html'

class ProductPageView(TemplateView):
    template_name = 'product-page.html'


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)
