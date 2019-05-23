from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# ViewSet视图集类继承于APIVIew和ViewSetMixin
# 将所有请求写在一个视图集中, 不在以请求方式区分, 以操作名区分

# GenericViewSet继承于ViewSetMixin和GenericAPIView可以直接搭配Mixin扩展类


class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

# 9个Mixin扩展类的子类继承了GenericAPIView和Mixin可以不用写get/post了
# Mixin中实现了list,create....中的通用代码封装
# 视图集GenericViewSet实现了list,create到get/post的映射和get_object等方法属性