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
        ]

