from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

@login_required(login_url='/login/')
def cart_index(request):
    return render(request, 'cart/index.html')


@login_required(login_url='/login/')
def checkout(request):
    uname = request.user.username
    u = User.objects.get(username=uname)
    return render(request, 'cart/checkout.html', {
        'total_amount': 200,
        'first_name': u.first_name,
        'last_name': u.last_name,
        'email': u.email,
    }
    )
