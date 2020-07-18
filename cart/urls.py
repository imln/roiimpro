from django.conf.urls import url
from user import views
from django.urls import path, include

# SET THE NAMESPACE!
from cart.views import cart_index, checkout

app_name = 'user'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('', cart_index, name='cart_index'),
    path('checkout/', checkout, name='checkout'),
]