from django.db import models

# Create your models here.
class Areas(models.Model):

    aid = models.CharField(max_length=30, primary_key=True)
    atitle = models.CharField(max_length=30)
    apid = models.ForeignKey('Areas',null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        # 表里默认显示的每一个对象ｏｂｊｅｃｔ，可以设置为
        return self.atitle

    class Meta:
        # 表名配置　数据库中　后台中
        db_table = 'areas'
        verbose_name = "地区表"
        verbose_name_plural = verbose_name  # 显示的复数名称


# 后台上传图片类
class PicUpload(models.Model):
    pic = models.ImageField(upload_to="user/")

    def __str__(self):
        return self.pic
    class Meta:
        db_table="picture"
        verbose_name = "上传图片"
        verbose_name_plural = verbose_name  # 显示的复数名称


# 图书模型类
class BookInfo(models.Model):
    """图书"""
    btitle = models.CharField(max_length=20, verbose_name="名称", db_column="书名")  # 站点字段名　与　数据库中的字段名
    bpub_date = models.DateField(verbose_name="出版日期")
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    def __str__(self):
        return self.btitle
    
    # 此方法作为后台显示字段,需有返回值
    def pub_date(self):
        return self.bpub_date
    pub_date.short_description = "发布日期"  # 方法的short..属性决定此字段名
    pub_date.admin_order_field = "bpub_date"  # 方法依哪个属性排序

    # 此方法访问关联英雄对象
    def hero_set(self):
        return self.heroinfo_set.all()
    hero_set.short_description = "关联英雄集"

    # 设置数据库中的表名与站点的表名
    class Meta:
        db_table = "book"
        verbose_name = "图书表"
        verbose_name_plural = verbose_name  # 显示的复数名称


class HeroInfo(models.Model):
    """英雄类"""
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name = "名称", db_column="英雄名")
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name="性别")
    hcomment = models.CharField(max_length=200 ,verbose_name="备注信息", null=True,blank=True)
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE,verbose_name="关联的图书")  # 外键
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    def __str__(self):
        return self.hname

    # 此方法访问关联对象属性，作为后台字段
    def book_name(self):
        return self.hbook.btitle
    # 设置此方法字段名
    book_name.short_description = "关联图书"
    book_name.admin_order_field = "hbook_id"

    class Meta:
        db_table = "hero"
        verbose_name = "英雄表"
        verbose_name_plural = verbose_name
