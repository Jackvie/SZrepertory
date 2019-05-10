from django.conf.urls import url

from orders import views


urlpatterns =[
    # 返回订单结算页面
    url(r'orders/settlement/$', views.OrderSettlementView.as_view()),
    # 提交订单接口
    url(r'^orders/commit/$', views.OrderCommitView.as_view()),
    # 订单提交成功时接口
    url(r'^orders/success/$', views.OrderSuccessView.as_view()),
    # 我的订单
    url(r'^orders/info/(?P<page_num>\d+)/$', views.UserOrderInfoView.as_view()),
]