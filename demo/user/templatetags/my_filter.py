# 格式比较固定 导入  {% load my_filter--过滤器所在文件名 %}
from django import template

register = template.Library()

@register.filter
def func1(num):
    # return num/2 错误,模板for循环的时候讲调用多次，但一次只传一个int
    return num%2

# {{ content|func2: val }}---左侧变量是第一参数，右侧：后是第二个参数
@register.filter
def func2(num,val):
    return num%val
