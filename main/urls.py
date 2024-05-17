from django.urls import path

from .views import login_view, main_page, register_view

urlpatterns = [
    path('', main_page, name='main'),
    path('login/' , login_view, name='login'),
    path('register/', register_view, name='register')
]