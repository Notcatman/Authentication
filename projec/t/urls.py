from django.urls import path
from .views import *

urlpatterns = [
    path('home/', base, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('access/', access, name='access'),
    path('logout/', logout_view, name='logout'),
]