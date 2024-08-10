from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'crud/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'crud/product_detail.html'
    context_object_name = 'product'
    paginate_by = 3

    class ProductCreateView(CreateView):
     model = Product
     fields = '__all__'
