from django.conf.urls import patterns, url
from blog import views
from feeds import LatestPostsFeed

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^blog/(?P<slug>[^\.]+).html', views.detail, name='detail'),
	url(r'^rss/feed', LatestPostsFeed()),
)
