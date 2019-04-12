from user import views
from django.conf.urls import url


urlpatterns = [
            url(r"^index/(?P<num>\d{2})/(?P<alpha>.)/$", views.index, name='index'),
            url(r"^change/$", views.change),
            url(r"^login/$", views.login),
            url(r"^login_check", views.login_check),
            url(r"^test1/$", views.test1, name="test1"),
            url(r"^test2/$", views.test2, name="test2"),
            url(r"^msg/$", views.msg),
            url(r"^prov/$", views.prov),
            url(r"^city(?P<pid>\d+)/$", views.city),
            url(r"^dis(?P<pid>\d+)/$", views.city),
            url(r"^pages_upload_images/$", views.pages_upload_images),
            url(r"^handle_images/$", views.handle_images),
            url(r"^dis_page(\d?)/$", views.dis_page),
            url(r"^test_request_META/$", views.test_request_META),
            url(r"^set_cookie/$", views.set_cookie),
            url(r"^get_cookie/$",views.get_cookie),
            url(r"^session_to_redis/$", views.session_to_redis),
            url(r"^register/$", views.RegisterView.as_view()),
            url(r"^form_func/$", views.form_func),
            url(r"^demo/$", views.DemoView.as_view()),
            url(r"^demo2/$", views.Demo2View.as_view()),
            url(r"^demo3/$", views.Demo3View.as_view()),
            url(r"^ask_ajax/$", views.ask_ajax),
            url(r"^for_ajax/$", views.for_ajax),
            url(r"^test_middleware/$", views.test_middleware),
            url(r"^test_django_filter/$", views.test_django_filter),
            url(r"^ismyfilter/$", views.ismyfilter),
            url(r"^dad/$", views.dad),
            url(r"^son/$", views.son),
        ]

