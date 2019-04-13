from django.contrib import admin
from user.models import Areas,PicUpload,BookInfo,HeroInfo

# 块嵌入　一类对象页面编辑多类
# class HeroInfoStackInline(admin.StackedInline):
#    model = HeroInfo  # 要编辑的对象　　多类
#    extra = 2  # 附加编辑的数量
# 表格嵌入　一类对象页面编辑多类
class HeroInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 1


# 继承后台管理admin.ModelAdmin
# ---不同与models.Manager是模型类管理器类
class BookInfoAdmin(admin.ModelAdmin):
    # 决定显示哪些字段　添加方法字段
    list_display = ["id","btitle", "bpub_date", "bread", "bcomment", "is_delete", "pub_date", "hero_set"]
    list_per_page = 3
    actions_on_bottom = True
    # 编辑页　每个具体对象的信息页　显示哪些属性 不能添加方法字段
    # fields = ['btitle', 'bpub_date', "bread", "bcomment"]
    # 分组fieldsets和fields会冲突
    fieldsets =(
                ('一',{
                    'fields':['btitle','bpub_date']  # 组一显示属性
                    }
                ),
                ('二',
                    {'fields':['bread','bcomment','image'],
                        'classes':('collapse',) # 是否折叠显示
                    }
                )
            )
    # 在一类中添加
    # inlines = [HeroInfoStackInline]  # 一类块编辑多类
    inlines = [HeroInfoTabularInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "hname", "hcomment", "hgender", "is_delete", "hbook_id", "book_name"]
    list_per_page = 4
    actions_on_bottom = True
    # 右侧过滤栏
    list_filter = ['hbook', 'hgender']
    # 搜索框
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
