# 格式比较固定 导入  {% load my_filter--过滤器所在文件名 %}
from django import template

register = template.Library()

@register.filter
def func1(num):
    # return num / 2
    return num

# 过滤的实质就是传过来一个列表字典元组，然后轮询每一个元素作为参数过滤，返回# 符合的元素集 filter属于高级语法，接受序列将每个元素判断返回符合情况的元素

@register.filter
def func2(num,value):
    return num
