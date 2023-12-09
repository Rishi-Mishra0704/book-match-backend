from django.core.management.base import BaseCommand
from api.models import Student, Book

class Command(BaseCommand):
    help = 'Seed data for Student and Book models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        Student.objects.create(name='Student 1', fiction_score=4, non_fiction_score=5)
        Student.objects.create(name='Student 2', fiction_score=3, non_fiction_score=8)
        Student.objects.create(name='Student 2', fiction_score=6, non_fiction_score=6)


        Book.objects.create(title='Book 1', author='Author 1', fiction_score=7, non_fiction_score=8)
        Book.objects.create(title='Book 2', author='Author 2', fiction_score=7, non_fiction_score=9)
        Book.objects.create(title='Book 3', author='Author 3', fiction_score=8, non_fiction_score=8)
        Book.objects.create(title='Book 4', author='Author 4', fiction_score=8, non_fiction_score=7)
        Book.objects.create(title='Book 5', author='Author 5', fiction_score=9, non_fiction_score=6)
        Book.objects.create(title='Book 6', author='Author 6', fiction_score=7, non_fiction_score=8)
        Book.objects.create(title='Book 7', author='Author 7', fiction_score=8, non_fiction_score=8)
        Book.objects.create(title='Book 8', author='Author 8', fiction_score=8, non_fiction_score=9)
        Book.objects.create(title='Book 9', author='Author 9', fiction_score=8, non_fiction_score=7)
        Book.objects.create(title='Book 10', author='Author 10', fiction_score=7, non_fiction_score=9)

        # Add more books as needed

        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
