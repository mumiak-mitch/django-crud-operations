from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.crud_list, name="crudlist"),
    path('form/', views.crud_form, name="crudform"),
    path('<int:id>/', views.crud_form, name="updateform"),
    path('delete/<int:id>/', views.crud_delete, name="cruddelete"),
]