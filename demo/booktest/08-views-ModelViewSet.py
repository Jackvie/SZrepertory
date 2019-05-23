from rest_framework.viewsets import ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

# 继承自GenericViewSet，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestoryModelMixin。

# ReadOnlyModelViewSet 继承自GenericViewSet，同时包括了ListModelMixin、RetrieveModelMixin。
# from rest_framework.viewsets import ReadOnlyModelViewSet