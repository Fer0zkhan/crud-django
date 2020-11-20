from django.contrib import admin
from .models import BookModel
# Register your models here.

from django_crud_app.admin_utils import set_admin

set_admin(BookModel, ('book_name', 'author_name'), ('book_name', 'author_name'),
          ('book_name', 'author_name', 'book_discription', 'publish_date'))
