from django.db import models

# Create your models here.
from django.urls import reverse


class ClientUsers(models.Model):
    full_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def edit_url(self):
        return reverse('edit_client', kwargs={'pk': self.pk})

    def delete_url(self):
        return reverse('delete_client', kwargs={'pk': self.pk})
