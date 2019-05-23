# from django.shortcuts import render
# from django.views import View
# from django.http import JsonResponse, HttpResponse, Http404
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
# import json

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer


# Create your views here.
# Mixin扩展来配合GenericAPIView使用
# 九个子类继承于GenericAPIView和Mixin扩展类的不同组合, 且封装了对应请求方法

# /books/
class BookListView(ListCreateAPIView):
    """
    获取所有图书、增加图书
    """
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()


# /books/(?P<pk>\d+)/
class BookDetailView(RetrieveUpdateDestroyAPIView):
    """
    获取、修改、删除指定图书
    """
    # 指定视图所使用的序列化器类
    serializer_class = BookInfoSerializer
    # 指定视图所使用的查询集
    queryset = BookInfo.objects.all()

