from django.shortcuts import render,redirect
from django.http import *
from django.urls import reverse
from user.models import Areas,PicUpload
from demo import settings
from django.core.paginator import Paginator
# Create your views here.

def index(request,num,alpha):
    return HttpResponse("jjjj%s%s" % (num,alpha))


def change(request):
    url = reverse("user:index", args=(11,0))
    return redirect(url)
    return render(request, 'user/index.html',{})


def login(request):
    return render(request, 'user/login.html',{})


def login_check(request):
    username2 = request.POST.get("username2")
    request.session["username2"] = username2
    print(request.session["username2"])
    return HttpResponse(username2)


def test1(request):
    res = HttpResponse(content="""{"a":1,"b":2}""", content_type="json", status="200")
    return res
    # return JsonResponse({"a":1,"b":2})


def test2(request):
    return render(request, 'user/test.html', {})
 

# 返回省市区的页面
def msg(request):
    return render(request, 'user/msg.html')


# 完成省请求的接口
def prov(request):
    province = Areas.objects.filter(apid_id__isnull = True)
    null_list = list()
    for i in province:
        null_list.append((i.aid,i.atitle))
    return JsonResponse({"data":null_list})


# 完成市,区请求接口
def city(request, pid):
    # obj = Areas.objects.get(aid=pid)
    # city_query_set = obj.areas_set.all()
    city_query_set = Areas.objects.filter(apid__aid__exact=pid)
    null_list = list()
    for i in city_query_set:
        null_list.append((i.aid, i.atitle))
    return JsonResponse({"data":null_list})


# 返回上传图片的页面
def pages_upload_images(request):
    return render(request, 'user/pages_upload_images.html', {})


# 上传图片的处理接口
def handle_images(request):
    pic = request.FILES['pic']
    pic_name = pic.name  # 获取图片的对象和图片名字

    # 创建一个文件用来存图片，先拼接路径
    pic_sys = settings.MEDIA_ROOT+"/user/"+pic_name
    with open(pic_sys, "wb") as f:
        for i in pic.chunks():  # chunks讲对象变为生成器
            f.write(i)
    p = PicUpload()
    p.pic = "user/%s" % pic_name
    p.save()  # 向数据库中添加一条记录

    return HttpResponse("存储完毕")


# 省级地区分页显示
def dis_page(request, num):

    # filter(多类过滤一类--关键属性__一类字段__判断)
    # filter(一类过滤多类--多类名小写__多类字段__判断)
    # filter(一类/多类过滤自身---自身字段__判断)
    area = Areas.objects.filter(apid__isnull=True)  # 返回省级地区所有信息对象查询集

    # 每页显示10条信息,创建Paginator类的对象
    paginator = Paginator(area, 10)

    # 创建Page类对象，返回第几页信息
    if num == "":
        num = 1
    page = paginator.page(int(num))
    return render(request,"user/dis_page.html",{"page":page})


def test_request_META(request):
    m = request.META
    m = (m["CONTENT_LENGTH"],m["CONTENT_TYPE"],m["HTTP_ACCEPT"],m["REMOTE_HOST"],m["REMOTE_ADDR"],m["REQUEST_METHOD"])
    return HttpResponse(m[-3])


def set_cookie(request):
    res = HttpResponseRedirect("/user/get_cookie")
    res.set_cookie("one","aaaa", max_age = 60)
    res.set_cookie("two","bbb", max_age = 60)
    return res


def get_cookie(request):
    try:
        print("-----------",request.COOKIES)
        print("-----------a",type(request.COOKIES))
        # if request.COOKIES.has_key("two"):
        #    print("7777777777777777")  # 字典没有has_key方法
        res = request.COOKIES["two"]
    except Exception as r:
        print(r)
        res = "error"
    return HttpResponse(res)


def session_to_redis(request):
    request.session["first"] = "lol"
    request.session["second"] = "olo"
    if "first" in request.session:
        print(">>>>>>>>>>>>>>>")
    try:
        print(request.session,request.session["first"],request.session["second"])
        print(request.session.get("first"),"ppppppppppppp")
        print(type(request.session),"-a-a-a-a-a-a")
    except Exception as e:
        print(e)
    return HttpResponse("session")


# 定义装饰器
def my_decorate(func):
    print("被装饰")
    def wrapper(request, *args, **kwargs):
        print("闭包被调用")
        print(request.path)
        return func(request, *args, **kwargs)
    return wrapper


from django.views.generic import View
class RegisterView(View):
    """类视图处理register的get/post/put请求"""
    def get(self, request):
        """处理get请求"""
        return HttpResponse("registerget")

    def post(self, request):
        """处理post请求"""
        return HttpResponse("registerpost")
 

def form_func(request):
    """访问表单，返回一个可以get/post的页面"""
    return render(request, "user/form_func.html", {})


from django.utils.decorators import method_decorator
# @method_decorator(my_decorate, name="get")
# @method_decorator(my_decorate, name="dispatch")
class DemoView(View):
    """处理demo的请求的类视图"""
    def get(self,request):
        return HttpResponse("demoget")
    
    @method_decorator(my_decorate)
    def post(self,request):
        return HttpResponse("demopost")

    def put(self,request):
        return HttpResponse("demoput")


# 类视图Mixin扩展类
class MyMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        print(super())
        view = super().as_view(*args, **kwargs)
        print(view)
        print("myMixin")
        view=my_decorate(view)
        print(view)
        return view


class Demo2View(MyMixin, View):
    def get(self, request):
        return HttpResponse("demo2get")

    def post(self, request):
        return HttpResponse("demo2post")


# 多继承Mixin扩展
class MyMixin2(object):
    def list(self, request, *args, **kwargs):
        print("ip:",self.request.META["REMOTE_ADDR"])


class MyMixin3(object):
    def create(self, request, *args, **kwargs):
        print(self.request.method)


class Demo3View(MyMixin2, MyMixin3, View):
    def get(self,request):
        self.list(request)
        return HttpResponse("demo3get")

    def post(self, request):
        self.create(request)
        return HttpResponse("demo3post")


# 请求一个内含ajax的模板文件
def ask_ajax(request):
    return render(request, "user/ask_ajax.html", {})


# ajax请求处理的接口
def for_ajax(request):
    ret = request.GET.get("a")
    print(ret)
    return JsonResponse({"c":2,"d":"dd"})


# 测试中间件
def test_middleware(request):
    print("我是视图函数")
    return HttpResponse("test_middleware")


# 测试django自带的过滤器
from datetime import *
def test_django_filter(request):
    return render(request, 'user/test_django_filter.html', {"data1":datetime(1996,7,2,13,45,12),"data2":[1,2,3,4,5],"data3":""})


# 自制过滤器
def ismyfilter(request):
    data1 = [1,2,3,4,5,6,7]
    return render(request, 'user/ismyfilter.html', {"data1":data1})


# jinjafilter过滤器
def isjinjafilter(request):
    data1 = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'user/isjinjafilter.html', {"data1":data1})

# 模板继承-父
def dad(request):
    return render(request, 'user/dad.html', {})

# 子
def son(request):
    return render(request, 'user/son.html', {})
