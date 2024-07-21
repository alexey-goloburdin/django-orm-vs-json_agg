from django.core.management.base import BaseCommand

from django.db import connection

def print_books_with_json():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                b.book_id,
                b.name AS book_name,
                json_agg(distinct a.*) AS authors,
                json_agg(distinct c.*) AS categories
            FROM book___ b
            LEFT JOIN book____authors USING(book_id)
            LEFT JOIN author___ a USING(author_id)
            LEFT JOIN book____categories USING(book_id)
            LEFT JOIN category___ c USING(category_id)
            GROUP by 1, 2
            ORDER BY b.name""")
        books = cursor.fetchall()
    for book in books:
        book_name = book[1]
        category_names = ", ".join([
            c["name"].lower() for c in book[3]
        ])
        author_names = ", ".join([
            a["name"] for a in book[2]
        ])
        print(f"«{book_name}», авторы: {author_names}, категории: {category_names}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        print_books_with_json()
