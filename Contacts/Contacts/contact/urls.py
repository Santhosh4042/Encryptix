from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Contact, name='index'),
    path('add/', views.AddContact, name='add'),
    path('search/', views.SearchContact, name='search'),
    path('update/<int:pk>/', views.UpdateContact, name='update'),
    path('delete/<int:pk>/', views.DeleteContact, name='delete'),
]
