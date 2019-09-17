from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_full_name = models.CharField(max_length=100)
    book_simple_name = models.CharField(max_length=32)
    book_image = models.FileField(max_length=1024)
    book_create_time = models.DateTimeField()
    book_last_update_time = models.DateTimeField()
    book_absract = models.CharField(max_length=1024)

    def __str__(self):
        return self.simple_name

class BookChacter(models.Model):
    book_id = models.foreign_key()
    chacter = models.BigIntegerField()
    chacter_name = models.CharField(max_length=100)
    chacter_content = models.TextField()

    def __str__(self):
        return self.book_content;

class BookChacterImage(models.Model):
    book_id = models.foreign_key()
    chacter = models.foreign_key()
    chacter_image = models.FileField(max_length=1024)

    def __str__(self):
        return self.book_id + ":" + self.chacter