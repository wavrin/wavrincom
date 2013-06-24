from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^blog/(?P<slug>[^\.]+).html', views.detail, name='detail'),
)