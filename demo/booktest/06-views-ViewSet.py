from rest_framework import viewsets, status
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# ViewSet视图集类继承于APIVIew和ViewSetMixin
# 将所有请求写在一个视图集中, 不在以请求方式区分, 以操作名区分

class BookInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            books = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookInfoSerializer(books)
        return Response(serializer.data)
