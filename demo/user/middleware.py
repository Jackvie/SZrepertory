from django.http import HttpResponse


def middleware_out(get_response):
    # print("外包")
    def middleware_in(request):
        # print("内包上")
        response = get_response(request)
        # print("内包下")
        # response = HttpResponse("no")
        return response
    return middleware_in

def my_middleware(get_response):
    # print('init 被调用')
    def middleware(request):
        # print('before request 被调用')
        response = get_response(request)
        # print('after response 被调用')
        return response
    return middleware


def my_middleware2(get_response):
    # print('init2 被调用')
    def middleware(request):
        # print('before request2 被调用')
        response = get_response(request)
        # print('after response2 被调用')
        return response
    return middleware


# 利用中间件阻止本机windows访问请求
def my_middleware3(get_response):
    print("无视图请求到来")
    # allowed_host = ["*"] runserver 192.168.118.129:8000
    Exclude_list = ["192.168.118.1"]
    def middleware(request):
        the_ip = request.META['REMOTE_ADDR']
        print('%s来了' % the_ip)
        if the_ip in Exclude_list:
            return HttpResponse("403forbidden")
        response = get_response(request)
        # print('after response2 被调用')
        return response
    return middleware
