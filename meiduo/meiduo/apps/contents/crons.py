import time,os
from django.shortcuts import render
from django.template import loader
from django.conf import settings

from contents.models import ContentCategory
from contents.utils import get_categories


def generate_static_index_html():
    """
    生成静态的主页html文件
    """
    print('%s: generate_static_index_html' % time.ctime())

    # 获取商品频道和分类
    categories = get_categories()

    # 广告内容
    contents = {}
    content_categories = ContentCategory.objects.all()
    for cat in content_categories:
        contents[cat.key] = cat.content_set.filter(status=True).order_by('sequence')

    # 渲染模板
    context = {
        'categories': categories,
        'contents': contents
    }

    # response = render(None, "index.html", context)
    # html_text = response.content.decode()
    temp = loader.get_template("index.html")
    html_text = temp.render(context)

    file_name = os.path.join(settings.STATICFILES_DIRS[0], "index.html")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_text)

