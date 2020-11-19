from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import ClientUsersSerializers
from .models import ClientUsers
from .client_utils import *


@api_view(['GET'])
def get_client_list(request):
    query_full_name = request.GET.get('full_name')
    query_email = request.GET.get('email')
    query_phone = request.GET.get('phone')

    if query_full_name:
        clients = ClientUsers.objects.filter(full_name__icontains=query_full_name)
    elif query_email:
        clients = ClientUsers.objects.filter(email__exact=query_email)
    elif query_phone:
        clients = ClientUsers.objects.filter(phone__icontains=query_phone)
    else:
        clients = ClientUsers.objects.all()

    serializer = ClientUsersSerializers(clients, many=True)

    if clients:
        client_data = success_response(serializer.data)
    else:
        client_data = failure_response(serializer.data, 'Request data not found')
    return Response(client_data)


@api_view(['GET'])
def get_client_list_by_id(request, pk):
    client = get_object_or_404(ClientUsers, pk=pk)
    serializer = ClientUsersSerializers(client)
    if client:
        client_data = success_response(serializer.data)
    else:
        client_data = failure_response(serializer.errors, 'Request Data Not Found')
    return Response(client_data)


@api_view(['POST'])
def post_client_data(request):
    serializer = ClientUsersSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        client_data = success_response(serializer.data)
    else:
        client_data = failure_response(serializer.data, 'Request Data Cant Add and Post')
    return Response(client_data)


@api_view(['PUT'])
def client_update(request, pk):
    client = get_object_or_404(ClientUsers, pk=pk)
    serializer = ClientUsersSerializers(data=request.data, instance=client)
    if serializer.is_valid():
        client_data = success_response(serializer.data)
    else:
        client_data = failure_response(serializer.errors, 'Request Data Cant Update')
    return Response(client_data)


@api_view(['DELETE'])
def client_delete(request, pk):
    client = get_object_or_404(ClientUsers, pk=pk)
    if client:
        client.delete()
        return Response(success_response('Data Deleted Successfully'))
    else:
        return Response(failure_response('Data Not Deleted ! Something Went Wrong!'))
