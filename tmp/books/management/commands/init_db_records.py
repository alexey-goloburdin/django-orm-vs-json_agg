from django.core.management.base import BaseCommand

from books.models import Author, Book, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()
        
        authors = (
            Author.objects.create(author_id=1, name='Александр Пушин'),
            Author.objects.create(author_id=2, name='Александр Беляев')
        )
        
        categories = (
            Category.objects.create(category_id=1, name='Художественная литература'),
            Category.objects.create(category_id=2, name='Научная фантастика')
        )
        
        book = Book.objects.create(
            book_id=1,
            name=f"Капитанская дочка"
        )
        book.categories.add(categories[0])
        book.authors.add(authors[0])
        
        book = Book.objects.create(
            book_id=2,
            name=f"Ариэль",
        )
        book.categories.add(categories[0], categories[1])
        book.authors.add(authors[1])

        book = Book.objects.create(
            book_id=3,
            name=f"Человек-амфибия",
        )
        book.categories.add(categories[0], categories[1])
        book.authors.add(authors[1])

        book = Book.objects.create(
            book_id=4,
            name=f"Голова профессора Доуэля",
        )
        book.categories.add(categories[0], categories[1])
        book.authors.add(authors[1])

