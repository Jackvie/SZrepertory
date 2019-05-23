from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# 视图集完成请求方式到action的映射, Generic添加查询集和序列化器类以及几个相应的属性方法
# action可以自己额外在视图集类中添加也可以继承Mixin类中的list,create等五个方法
# 也可以直接继承ModelViewSet则拥有了五个方法和请求到操作的映射和Generic的属性方法

class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 视图集中添加额外的处理方法
    def latest(self, request):
        """获取最新图书"""
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """
        # book = self.get_object()
        # serializer = self.get_serializer(book, data=request.data)
        # serializer.is_valid()
        # return Response(serializer.data, status=status.)
        # 这儿request.data只修改阅读量一个属性,这样反序列校验时别的属性参数可能要求你传,这样只传阅读量就会失败
        # 如果只传一个属性修改,用原始方法
        book = self.get_object()
        book.bread = request.data.get("bread")
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
        # 或者重写get_serializer_class()方法返回一个只有一个字段的序列化器类
        # def get_serializer_class(self):
        #    if self.action == "latest":
        #       return  MySerializer
        #    else:
        #       return self.serializer_class

