from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.mainhome, name = 'mainhome'),
    path('create/', views.create, name = 'create'),
    path('edit/<int:bookmark_id>', views.edit, name = 'edit'),
    path('delete/<int:bookmark_id>', views.delete, name = 'delete'),
]