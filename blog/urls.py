from django.urls import path, include
from blog.views import home,articles

urlpatterns = [
    path("", home, name="home"),
    path('articles/<int:pid>', articles,name="articles")
]
