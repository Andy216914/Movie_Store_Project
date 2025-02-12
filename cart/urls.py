from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='cart.index'),
    path('<int:id>/add/', views.add, name='cart.add'),
    path('clear/', views.clear, name='cart.clear'),
    path('<int:id>/remove/', views.remove, name='cart.remove'),
    path('purchase/', views.purchase, name='cart.purchase'),
]