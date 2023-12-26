from django.contrib import admin
from django.urls import path
from . import views
from .views import BookListView

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews/', views.create_review, name='create_review'), 
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:book_id>/', views.book_more_info, name='book_more_info'),
    path('staff/', views.staff_settings, name='staff_settings'),
    path('staff/add_book/', views.add_book, name='add_book'),
    path('staff/<int:book_id>/modify/', views.modify_books, name='modify_books'),
    path('staff/view_books/', views.view_books, name='view_books'),
    path('staff/add_book/', views.delete_books, name='delete_books'),
    
]
