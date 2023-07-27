from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from blog.models import *
import markdown
from django.core.paginator import Paginator
def homepage(request):
    return render(request, "homepage.html")

def home(request):
    value = {}
    tagid = request.GET.get('tid',0)
    # pid = request.GET.get('page','0')
    tags = Tags.objects.all();
    # passages = []
    if tagid == 0:
        passages = Passages.objects.filter(is_proj=False).order_by('-create_timestamp')
    else:
        passages = Passages.objects.filter(tagid_id = tagid,is_proj=False).order_by('-create_timestamp')

    tagcontexts = []
    
    for p in passages:
        t = Tags.objects.get(tagid = p.tagid_id).tagcontext   
        tagcontexts.append(t)
        
    #value['passages'] = zip(passages,tagcontexts)
    paginator = Paginator(list(zip(passages,tagcontexts)), 9)
    num_p = request.GET.get('page', 1)
    page = paginator.page(int(num_p))
    value['page'] = page
    value['passages'] = passages

    value['tags'] = tags
    value['curr_tagid'] = int(tagid)

    return render(request, "home.html",value)

# Create your views here.
def articles(request):
    pid = request.GET.get('pid',1)
    passage = Passages.objects.get(pid=pid)
    tagid = Passages.objects.get(pid = passage.pid)
    passages = Passages.objects.filter(tagid_id = tagid.tagid_id)
    html = markdown.markdown(passage.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    passage.viewcount = passage.viewcount + 1
    passage.save()
    
    # locals()代替了context，locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典
    return render(request,"articles.html",locals())
    
def projects(request):
    return render(request, "projects.html")

def proj_context(request):
    proj_id = request.GET.get('proj',0)
    proj = Passages.objects.get(pid=proj_id)

    return render(request, "project.html",locals())