from django.urls import path
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from mysite.models import Articles
from . import views

urlpatterns = [
    url('^$', views.index, name = 'index'),
    url('^contact/$', views.contact, name='contact'),
    url('^news/$',
        ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name = "mysite/news.html")),
    url('^news/(?P<pk>\d+)', DetailView.as_view(model=Articles, template_name="mysite/post.html")),
    url('^reset/$', views.reset, name='reset'),
    url('^reset_user/$', views.reset_user, name='reset_user')
]