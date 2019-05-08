from django.conf.urls import url

from orders import views


urlpatterns =[
    # 返回订单结算页面
    url(r'orders/settlement/$', views.OrderSettlementView.as_view()),
]