from django.urls import path
from .views_api import *

urlpatterns = [
    path('books/', get_post_data, name='get-post-data'),
    path('books/<int:pk>', find_by_id_update_delete, name='findbyid-update-delete'),
]
