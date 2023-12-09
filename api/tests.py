from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Student, Book
from .serializers import StudentSerializer, BookSerializer

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(name="John", fiction_score=8, non_fiction_score=6)
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", fiction_score=7, non_fiction_score=5)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", fiction_score=6, non_fiction_score=4)

    def test_students_view(self):
        url = reverse('students')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student_view(self):
        url = reverse('create_student')
        data = {"name": "John Doe", "fiction_score": 8, "non_fiction_score": 6}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_books_view(self):
        url = reverse('books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_view(self):
        url = reverse('create_Book')
        data = {"title": "New Book", "author": "New Author", "fiction_score": 7, "non_fiction_score": 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_matching_books_view(self):
        url = reverse('matching_books')
        data = {"student_id": self.student.id, "fiction_score": 8, "non_fiction_score": 6}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
