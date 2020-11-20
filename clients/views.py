from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import ClientUsers
from .tables import ClientUsersTable
from .forms import ClientUsersForm


# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'client_DashBoard_url': reverse('home'),
        'book_dashboard_url': reverse('books_home')
    }
    return render(request, 'index.html', context)


def home(request):
    clients = ClientUsers.objects.all()
    sort = request.GET.get('sort', None)
    if sort:
        clients = clients.order_by(sort)
    table = ClientUsersTable(clients)
    context = {
        'table': table,
        'data_exits': clients,
        'title': 'Client',
        'home_page_url': reverse('index'),
        'add_page_url': reverse('add_client')
    }
    return render(request, 'home.html', context)


def add_client(request):
    if request.method == 'POST':
        form = ClientUsersForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('home')
    else:
        form = ClientUsersForm()
    context = {
        'form': form,
        'title': 'Add New User',
        'dashBoard_url': reverse('home')
    }
    return render(request, 'add-edit-form.html', context)


def edit_client(request, pk):
    client = get_object_or_404(ClientUsers, pk=pk)
    if request.method == 'POST':
        form = ClientUsersForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientUsersForm(instance=client)
    context = {
        'title': 'Edit User',
        'form': form,
        'dashBoard_url': reverse('home')
    }
    return render(request, 'add-edit-form.html', context)


def delete_client(request, pk):
    client = get_object_or_404(ClientUsers, pk=pk)
    client.delete()
    return redirect('home')


