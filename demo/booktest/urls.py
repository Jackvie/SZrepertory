from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
]
