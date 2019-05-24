from rest_framework import mixins, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# 视图集完成请求方式到action的映射, Generic添加查询集和序列化器类以及几个相应的属性方法
# action可以自己额外在视图集类中添加也可以继承Mixin类中的list,create等五个方法
# 也可以直接继承ModelViewSet则拥有了五个方法和请求到操作的映射和Generic的属性方法

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 设置视图的认证方案
    authentication_classes = [SessionAuthentication]
    # 指定某个视图所使用的权限控制类
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    # 指定正则
    lookup_value_regex = "\d+"
    #  自写方法router时detail为true会生产正则

    # 视图集中添加额外的处理方法
    @action(methods=["get"], detail=False)
    def latest(self, request):
        """获取最新图书"""
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    @action(methods=["PUT"], detail=True)
    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """

        book = self.get_object()
        book.bread = request.data.get("bread")
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)

