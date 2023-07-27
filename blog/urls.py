from django.urls import path, include
from blog.views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("articles/", home, name="home"),
    # path("articles/?tid=<int:tid>/?page=<int:page>", home, name="home"),
    path('article/', articles,name="articles"),
    path("projects", projects, name="projects"),
    path("projects/?proj=<int:projid>/",proj_context, name="proj_context")
    #path('articles/<int:tagid>', views.playing),
]
