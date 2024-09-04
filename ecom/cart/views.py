from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
     cart = Cart(request)
     cart_products = cart.get_prods
     quantity = cart.get_quants
     return render(request,'summary.html',{'cart_products':cart_products, 'cart_quantity':quantity})

def cart_add(request):
     # Get the cart
     cart =  Cart(request)
     # test for post
     if request.POST.get('action') == 'post':
          #Get stuff
          product_id = int(request.POST.get('product_id'))
          product_qty = int(request.POST.get('product_qty'))
          # look up product in DB
          product = get_object_or_404(Product, id=product_id)
          #save to session
          cart.add(product=product, quantity= product_qty)
          #get cart quantity
          cart_quantity = cart.__len__()
          response = JsonResponse({'qty': cart_quantity})
          return response


def cart_update(request):
     pass


def cart_delete(request):
      pass
