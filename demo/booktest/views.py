from django.db import DatabaseError
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    """测试自定义异常处理函数"""
    def get(self, request):
        raise DatabaseError
