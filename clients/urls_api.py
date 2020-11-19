from django.urls import path
from .view_api import *

urlpatterns = [
    path('clients/add', post_client_data, name='client-add'),
    path('clients', get_client_list, name='client-list'),
    path('clients/<int:pk>', get_client_list_by_id, name='client-list-by-id'),
    path('clients/update/<int:pk>', client_update, name='client-update'),
    path('clients/delete/<int:pk>', client_delete, name='client-delete'),
]
