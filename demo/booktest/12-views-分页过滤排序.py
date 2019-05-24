from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

class StandardResultPagination(PageNumberPagination):
    """自定义分页类
    page_size 每页数目,页容量
    page_query_param 前端发送的页数关键字名，默认为"page"
    page_size_query_param 前端发送的每页数目关键字名，默认为None
    max_page_size 前端最多能设置的每页数量"""
    page_size = 2
    page_size_query_param = 'page_size'  # 定义请求参数中指定页容量的关键字名
    max_page_size = 4  # 请求中最大页容量
    #  http://api.example.org/books/?page=<页码>&page_size=<页容量>


# 过滤排序 分页 只对于列表数据有效
class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 视图中添加filter_fields属性，指定可以过滤的字段
    filter_fields = ('btitle', 'bread')
    # 127.0.0.1:8000/books/?btitle=西游记

    # 指定排序字段
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'bread', 'bpub_date')
    # 127.0.0.1:8000/books/?ordering=-bread

    # # 指定当前视图所使用的分页类
    pagination_class = StandardResultPagination
    # 关闭分页类
    # pagination_class = None


