# from django.shortcuts import render
# from django.views import View
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
# import json

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer


# Create your views here.
# Mixin扩展来配合GenericAPIView使用

# /books/
class BookListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    获取所有图书、增加图书
    """
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request):
        """
        获取所有的图书数据
        """
        return self.list(request)

    def post(self, request):
        """
        新增一个图书数据
        """
        return self.create(request)

# /books/(?P<pk>\d+)/
class BookDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    获取、修改、删除指定图书
    """
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        """
        获取指定图书
        """
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """
        修改指定图书
        """
        return self.update(request, pk)

    def delete(self, request, pk):
        """
        删除指定图书：
        """
        return self.destroy(request, pk)
