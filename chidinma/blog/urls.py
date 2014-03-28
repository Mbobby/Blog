from django.conf.urls import patterns, include, url
from blog.views import index, all_articles, get_article, create, like, comment

urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^all/$', all_articles),
	url(r'^create/$', create), 
	url(r'^get/(?P<article_id>\d+)/$', get_article),
	url(r'^like/(?P<article_id>\d+)/$', like),
	url(r'^comment/(?P<article_id>\d+)/$', comment), 
	)