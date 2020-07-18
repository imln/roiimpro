from django.conf.urls import url
from user import views
from django.urls import path, include

# SET THE NAMESPACE!
from user.views import user_login, user_logout, index, register

app_name = 'user'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
