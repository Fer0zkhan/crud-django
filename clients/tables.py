import django_tables2 as tables
from django.utils.html import format_html

from .models import ClientUsers


class ClientUsersTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {'class': 'table table-dark mt-3'}
        model = ClientUsers

    def render_actions(self, value, record):
        return format_html(
            "<a href='{}' class='btn btn-primary btn-sm'>Edit</a>"
            "<a href='{}' class='btn btn-danger btn-sm ml-2'>Delete</a>".format(record.edit_url(), record.delete_url())
        )
