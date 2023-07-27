from django.contrib import admin
from django.db import models
from blog.models import Tags,Passages
from mdeditor.widgets import MDEditorWidget

# class ArticlesAdmin(admin.ModelAdmin):
#     # 后台要显示的字段
#     list_display = ['pid','viewcount','title','describtion','tag','create_timestamp']
#     formfield_overrides = {
#         models.TextField: {'widget': MDEditorWidget}
#     }
#     # 每页的数据条数
#     list_per_page = 20
    # 后台数据列表排序方式
    # ordering = {'create_timestamp'}
class PassagesAdmin(admin.ModelAdmin):
     # 后台要显示的字段
    list_display = ['pid','viewcount','title','describtion','tagid_id','create_timestamp','is_proj']
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    # 每页的数据条数
    list_per_page = 20

class TagsAdmin(admin.ModelAdmin):
    list_display = ['tagid','tagcontext']

# admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Passages,PassagesAdmin)