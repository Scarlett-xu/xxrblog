from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from blog.models import *
import markdown
def home(request):
    value = {}
    passages = Articles.objects.all()
    value['passages'] = passages
    return render(request, "home.html",value)

# Create your views here.
def articles(request,pid):
    passage = Articles.objects.get(pid=pid)
    passages = Articles.objects.all()
    html = markdown.markdown(passage.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    passage.viewcount = passage.viewcount + 1
    passage.save()
    # locals()代替了context，locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典
    return render(request,"articles.html",locals())