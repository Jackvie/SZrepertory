from django.conf.urls import url
from booktest import views

urlpatterns =[
    url(r'tests/$', views.TestView.as_view()),
]