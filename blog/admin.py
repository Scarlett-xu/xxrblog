from django.contrib import admin
from django.db import models
from blog.models import Articles
from mdeditor.widgets import MDEditorWidget

class ArticlesAdmin(admin.ModelAdmin):
    # 后台要显示的字段
    list_display = ['viewcount','title','pid','describtion','tag','create_timestamp']
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    # 每页的数据条数
    list_per_page = 20
    # 后台数据列表排序方式
    # ordering = {'create_timestamp'}



admin.site.register(Articles, ArticlesAdmin)