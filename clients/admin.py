from django.contrib import admin
from .models import ClientUsers
from django_crud_app.admin_utils import set_admin

# Register your models here.
# admin.site.register(ClientUsers)
set_admin(ClientUsers, ('full_name', 'email', 'phone'), ('full_name', 'email', 'phone'),
          ('full_name', 'email', 'phone', 'created_at'))
