from django.urls import path
from .views import index, book_details, book_delete, book_create, book_update
app_name= 'home'
urlpatterns = [
    path('', index, name='home'),
    path('details/<int:pk>', book_details, name='book-details'),
    path('delete/<int:pk>', book_delete, name='book-delete'),
    path('create', book_create, name='book-create'),
    path('update/<int:pk>', book_update, name='book-update'),
]