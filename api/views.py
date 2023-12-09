from django.shortcuts import render
from rest_framework import status
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Book
from .serializers import StudentSerializer, BookSerializer

# Create your views here.

@api_view(['GET'])
def students(request):
    """
    View to retrieve a list of all students.

    Parameters:
    - request: HTTP request object

    Returns:
    - Response: Serialized data of all students with HTTP status code
    """
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_student(request):
    """
    View to create a new student.

    Parameters:
    - request: HTTP request object containing data for the new student

    Returns:
    - Response: Serialized data of the created student with HTTP status code
    """
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def books(request):
    """
    View to retrieve a list of all books.

    Parameters:
    - request: HTTP request object

    Returns:
    - Response: Serialized data of all books with HTTP status code
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_Book(request):
    """
    View to create a new book.

    Parameters:
    - request: HTTP request object containing data for the new book

    Returns:
    - Response: Serialized data of the created book with HTTP status code
    """
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def matching_books(request):
    """
    Endpoint to retrieve matching books based on a student's preferences.

    Parameters:
    - request: HTTP POST request object containing data for matching books.
      - student_id: The unique identifier of the student.
      - fiction_score: The score for the student's preference in fiction books (default is 0).
      - non_fiction_score: The score for the student's preference in non-fiction books (default is 0).

    Algorithm:
    1. Extracts the `student_id`, `fiction_score`, and `non_fiction_score` from the request data.
    2. Attempts to retrieve the student from the database using the provided `student_id`.
       - If the student is not found, returns a 404 error with an appropriate error message.
    3. Calculates the differences between the student's preference scores and the scores of each book in the database.
       - Uses annotations to create two additional fields: `question_1_diff` and `question_2_diff`.
         - `question_1_diff`: Difference between the student's fiction score and the book's fiction score.
         - `question_2_diff`: Difference between the student's non-fiction score and the book's non-fiction score.
    4. Filters books based on the calculated differences, ensuring they fall within the range of [-2, 2].
    5. Uses a serializer (`BookSerializer`) to convert the matching books into a serialized format.
    6. Returns a response with the serialized data of matching books and an HTTP status code of 200.
       - If the student is not found, returns a 404 error with an error message.
       - If the request method is not POST, returns a 400 error with an error message.

    Returns:
    - Response: Serialized data of the matching books with an HTTP status code.
      - If successful, returns a list of matching books.
      - If the student is not found, returns a 404 error with an error message.
      - If the request method is not POST, returns a 400 error with an error message.
"""

    if request.method == 'POST':
        student_id = request.data.get('student_id')
        fiction_score = int(request.data.get('fiction_score', 0))
        non_fiction_score = int(request.data.get('non_fiction_score', 0))

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        matching_books = Book.objects.annotate(
            question_1_diff=F('fiction_score') - fiction_score,
            question_2_diff=F('non_fiction_score') - non_fiction_score,
        ).filter(
            question_1_diff__gte=-2,
            question_1_diff__lte=2,
            question_2_diff__gte=-2,
            question_2_diff__lte=2,
        )

        # Serialize the matching books
        serializer = BookSerializer(matching_books, many=True)

        # Return the serialized data with HTTP status code
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)
