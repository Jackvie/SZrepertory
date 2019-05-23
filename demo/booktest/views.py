from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, Http404

from booktest.models import BookInfo, HeroInfo
# Create your views here.

from booktest.serializers import BookInfoSerializer

# /books/
class BookListView(View):
    """
    获取所有图书、增加图书
    """
    def get(self, request):
        """
        获取所有的图书数据
        """
        queryset = BookInfo.objects.all()

        # 序列化所有图书数据
        serializer = BookInfoSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        新增一个图书数据
        """
        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 反序列化-数据校验
        serializer = BookInfoSerializer(data=book_dict)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(save内部会调用序列化器类的create方法)
        serializer.save()

        return JsonResponse(serializer.data, status=201)

# /books/(?P<pk>\d+)/
class BookDetailView(View):
    """
    获取、修改、删除指定图书
    """
    def get(self, request, pk):
        """
        获取指定图书
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 将图书数据进行序列化
        serializer = BookInfoSerializer(book)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        """
        修改指定图书
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 反序列化-数据校验
        serializer = BookInfoSerializer(book, data=book_dict)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(save内部会调用序列化器类的update方法)
        serializer.save()

        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        """
        删除指定图书：
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)
