from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/login/')
def cart_index(request):
    return render(request, 'cart/index.html')


@login_required(login_url='/login/')
def checkout(request):
    return render(request, 'cart/checkout.html')
