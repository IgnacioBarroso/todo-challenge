from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update_status/<int:id>', views.update_status, name='update_status'),
    path('register', views.register, name='register'),
]
