from django.db import models
from mdeditor.fields import MDTextField
# import django
class Articles(models.Model):
    viewcount = models.IntegerField(default=1) #阅读次数
    title = models.CharField(max_length=300, default='title') #标题
    pid = models.IntegerField(default=1) #passage id
    describtion = models.CharField(max_length=300, default='describtion')
    tag = models.CharField(max_length=100, default='tag')
    content = MDTextField()
    create_timestamp = models.DateTimeField(auto_now_add=True)
    # pic = models.ImageField(upload_to='media/') #封面图
    # surface_img = models.ImageField(upload_to="surface_img/", null=True, blank=True, verbose_name="文章封面图")
    # surface_img = models.CharField(max_length=100)
