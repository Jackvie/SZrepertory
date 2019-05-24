from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

# 自定义异常处理函数
def exception_handler(exc, context):  # exc异常对象 context['view']当前异常发生的哪个类的类名
    # 先调用DRF框架的默认异常处理函数
    response = drf_exception_handler(exc, context)
    if response is None:
        if isinstance(exc, DatabaseError):
            # 补充数据库的异常处理
            response = Response({'default': 'DatabaseError'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response