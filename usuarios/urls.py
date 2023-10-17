from django.urls import path
from usuarios.views import some_view

urlpatterns = [
    path('',some_view, name='index.html'),
]
