from django.http import HttpResponse


def middleware_out(get_response):
    print("外包")
    def middleware_in(request):
        print("内包上")
        response = get_response(request)
        print("内包下")
        # response = HttpResponse("no")
        return response
    return middleware_in

def my_middleware(get_response):
    print('init 被调用')
    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response
    return middleware


def my_middleware2(get_response):
    print('init2 被调用')
    def middleware(request):
        print('before request2 被调用')
        response = get_response(request)
        print('after response2 被调用')
        return response
    return middleware
