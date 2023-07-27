from django.db import models
from mdeditor.fields import MDTextField
# import django
class Tags(models.Model):
    tagid = models.AutoField(primary_key=True)
    tagcontext = models.CharField(max_length=300, default='tagcontext')

# class Articles(models.Model):
#     # 主键
#     pid = models.AutoField(primary_key=True) #passage id
#     viewcount = models.IntegerField(default=1) #阅读次数
#     title = models.CharField(max_length=300, default='title') #标题
    
#     describtion = models.CharField(max_length=300, default='describtion')
#     # 外键
#     # tagid = models.ForeignKey(Tags,on_delete=models.CASCADE) 
#     tag = models.CharField(max_length=100, default='tag')
#     content = MDTextField()
#     create_timestamp = models.DateTimeField(auto_now_add=True)
#     # pic = models.ImageField(upload_to='media/') #封面图
#     # surface_img = models.ImageField(upload_to="surface_img/", null=True, blank=True, verbose_name="文章封面图")
#     # surface_img = models.CharField(max_length=100)


class Passages(models.Model):
     # 主键
    pid = models.AutoField(primary_key=True) #passage id
    viewcount = models.IntegerField(default=1) #阅读次数
    title = models.CharField(max_length=300, default='title') #标题
    
    describtion = models.CharField(max_length=300, default='describtion')
    # 外键
    tagid = models.ForeignKey(Tags,on_delete=models.CASCADE) 
    content = MDTextField()
    create_timestamp = models.DateTimeField(auto_now_add=True)

    is_proj = models.BooleanField(default=False)
    defaultlink = "https://xxrblog.oss-cn-nanjing.aliyuncs.com/Snipaste_2023-01-16_14-59-04.png"
    Surface_img = models.CharField(max_length=100,default=defaultlink)
    # tagcontext = models.ManyToManyField(to = "Tags")