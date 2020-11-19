from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import BookModelSerializer
from .models import BookModel
from .utils import *


@api_view(['GET', 'POST'])
def get_post_data(request):
    if request.method == 'POST':
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(success_response(serializer.data, 'Request Data Successfully Post'))
        else:
            return Response(failure_response(serializer.errors, 'Request Data Failure'))

    elif request.method == 'GET':
        query_book_name = request.GET.get('book_name')
        query_author_name = request.GET.get('author_name')
        query_book_discription = request.GET.get('book_discription')

        if query_book_name:
            book = BookModel.objects.filter(book_discription__icontains=query_book_name)
        elif query_author_name:
            book = BookModel.objects.filter(author_name__icontains=query_author_name)
        elif query_book_discription:
            book = BookModel.objects.filter(book_discription__icontains=query_book_discription)
        else:
            book = BookModel.objects.all()
        serializer = BookModelSerializer(book, many=True)
        if book:
            return Response(success_response(serializer.data, 'Request Data Successfully Get'))
        else:
            return Response(failure_response(serializer.data, 'Request Error Fail To Fetch Data'))


@api_view(['PUT', 'DELETE', 'GET'])
def find_by_id_update_delete(request, pk):
    book = get_object_or_404(BookModel, pk=pk)

    if request.method == 'GET':
        serializer = BookModelSerializer(book)
        if book:
            return Response(success_response(serializer.data, 'Request Data Seccessfully Find'))
        else:
            return Response(failure_response(serializer.data, 'Request Data Cant Find Successfully!'))

    elif request.method == 'PUT':
        serializer = BookModelSerializer(data=request.data, instance=book)
        if serializer.is_valid():
            book = serializer.save()
            serializer = BookModelSerializer(book)
            return Response(success_response(serializer.data, 'Request Data Succesfully Updated'))
        else:
            return Response(failure_response(serializer.errors, 'Request Data Failure And Fail to Update'))

    elif request.method == 'DELETE':
        if book:
            book.delete()
            return Response(success_response('Request Data Successfully Deleted'))
        else:
            return Response(failure_response('Request Data cant Delete'))
