from django.shortcuts import render

# Create your views here.
def cart_summary(request):
     return render(request,'summary.html')

def cart_add(request):
    pass
    if request.POST.get('action') = 'post':

def cart_update(request):
     pass


def cart_delete(request):
      pass
