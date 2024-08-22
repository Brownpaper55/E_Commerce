from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
     return render(request,'summary.html')

def cart_add(request):
     # Get the cart
     cart =  Cart(request)
     # test for post
     if request.POST.get('action') == 'post':
          #Get stuff
          product_id = int(request.POST.get('product_id'))
          # look up product in DB
          product = get_object_or_404(Product, id=product_id)
          #save to session
          cart.add(product=product)
          response = JsonResponse({'Product name: ': product.name})
          return response


def cart_update(request):
     pass


def cart_delete(request):
      pass
