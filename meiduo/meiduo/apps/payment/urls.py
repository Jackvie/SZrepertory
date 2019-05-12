from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^payment/(?P<order_id>\d+)/$', views.PaymentView.as_view()),
    # http://www.meiduo.site:8000/payment/status/?charset=utf-8&out_trade_no=20190512090908000000001&method=alipay.trade.page.pay.return&total_amount=3798.00&sign=l%2F3hjcidhXeEOvoGEiqvyxFzttEDW%2FmHvpWY9miCJ9VfrvLkyfDZumJpcYua%2Bib2hiljsENWHvE9Ig4plUkm1shXdLyWaGaKDFGmC0z7xW%2FpEU4UNSX2Q0Z2v%2Bw50SvtLKzJOgqGHAdjup%2FJqpKfgqDLquMjRt4yFLyk%2FhyVto5ciSsKJvQWrrYvhSiysY0UMJaM%2FqKg1N3h7KjNzRoLl3jqmkhTtgZajiBQDNwSjmIvlxTJLr%2BZVjcdNvrhJQs1JQYyze%2BgMYGE%2FltA2wlKTLEvalB1hAa3VBZtKD%2Bd1Wf7NZJcSQm8YdoBXUqlvjDKx4r5Pz8EYqki3I2VB4rASA%3D%3D&trade_no=2019051222001453201000008495&auth_app_id=2016092900622911&version=1.0&app_id=2016092900622911&sign_type=RSA2&seller_id=2088102177787118&timestamp=2019-05-12+17%3A12%3A37
    url(r'^payment/status/$', views.PaymentStatusView.as_view()),  # 回调地址
]