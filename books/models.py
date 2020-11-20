from django.db import models


# Create your models here.
from django.urls import reverse


class BookModel(models.Model):
    book_name = models.CharField(max_length=20, blank=False, null=False)
    author_name = models.CharField(max_length=20, blank=False, null=False)
    book_discription = models.TextField(max_length=200, blank=False, null=False)

    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name

    def edit_book(self):
        return reverse('edit_book', kwargs={'pk': self.pk})

    def delete_book(self):
        return reverse('delete_book', kwargs={'pk': self.pk})
