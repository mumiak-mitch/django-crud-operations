from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.crud_form, name="crudform"),
    path('<int:id>/', views.crud_form, name="updateform"),
    path('list/', views.crud_list, name="crudlist"),
    path('delete/<int:id>/', views.crud_delete, name="cruddelete"),
]