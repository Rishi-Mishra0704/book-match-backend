from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.students, name='students'),
    path('student/create/', views.create_student, name='create_student'),
    path('books/', views.books, name='books'),
    path('book/create/', views.create_Book, name='create_Book'),
    path('student/matching_books/', views.matching_books, name='matching_books'),
]
