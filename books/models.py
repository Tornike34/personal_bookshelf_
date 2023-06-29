from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, default="Name")
    last_name = models.CharField(max_length=100, default="Last_name")
    age = models.IntegerField()
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
