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
