from django.db import models

# Create your models here.
class Areas(models.Model):

    aid = models.CharField(max_length=30, primary_key=True)
    atitle = models.CharField(max_length=30)
    apid = models.ForeignKey('Areas',null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'areas'

# 后台上传图片类
class PicUpload(models.Model):
    pic = models.ImageField(upload_to="user/")
    class Meta:
        db_table="picture"


# 图书模型类
class BookInfo(models.Model):
    """图书"""
    btitle = models.CharField(max_length=20, verbose_name="名称", db_column="书名")  # 站点字段名　与　数据库中的字段名
    bpub_date = models.DateField(verbose_name="出版日期")
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    def __str__(self):
        return self.btitle

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

    class Meta:
        db_table = "hero"
        verbose_name = "英雄表"
        verbose_name_plural = verbose_name
