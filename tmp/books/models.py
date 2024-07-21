from django.db import models

class Author(models.Model):
    author_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "author___"

class Category(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "category___"

class Book(models.Model):
    book_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(to=Author, related_name='books')
    categories = models.ManyToManyField(to=Category, related_name='books')

    class Meta:
        db_table = "book___"
