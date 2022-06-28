from django.test import TestCase

# Create your tests here.
from catalog.models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='Rich Dad Poor Dad', author='Robert Kiyoski')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_genre_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('genre').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_title_by_author(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title} by {book.author}'
        self.assertEqual(str(book), expected_object_name)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')
