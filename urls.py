from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('',
	# ex: /reviews/
    url(r'^$', views.index, name='index'),
    # ex: /reviews/4/
    url(r'^(?P<review_id>\d+)/$', views.detail, name='detail'),
)
