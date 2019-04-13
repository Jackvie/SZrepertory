from django.contrib import admin
from user.models import Areas,PicUpload,BookInfo,HeroInfo

# 继承后台管理admin.ModelAdmin
# ---不同与models.Manager是模型类管理器类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id","btitle", "bpub_date", "bread", "bcomment", "is_delete", "pub_date", "hero_set"]
    list_per_page = 3
    actions_on_bottom = True


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hcomment", "hgender", "is_delete", "hbook_id", "book_name"]
    list_per_page = 4
    actions_on_bottom = True
    list_filter = ['hbook', 'hgender']
    search_fields = ["hname"]


# Register your models here.
admin.site.register(Areas)
admin.site.register(PicUpload)

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

# site--位置
admin.site.site_header = "这是网站页头"
admin.site.site_title = "这是网页标题"
admin.site.index_title = "这是欢迎标语"
