from django.urls import path, include
from blog.views import home,articles,homepage

urlpatterns = [
    path("", homepage, name="homepage"),
    path("home", home, name="home"),
    path('articles/<int:pid>', articles,name="articles")
]
