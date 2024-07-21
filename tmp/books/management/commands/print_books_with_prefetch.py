from django.core.management.base import BaseCommand

from books.models import Book


def print_books_with_prefetch():
    books = Book.objects.prefetch_related("authors", "categories").all()
    for book in books:
        book_name = book.name
        category_names = ", ".join([
            c.name.lower() for c in book.categories.all()
        ])
        author_names = ", ".join([
            a.name for a in book.authors.all()
        ])
        print(f"«{book_name}», авторы: {author_names}, категории: {category_names}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print_books_with_prefetch()
