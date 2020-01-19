from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [

	# /blog/
	url(r'^$', views.index, name='index'),

	# /blog/3/
	url(r'^(?P<post_id>[0-9]+)/$', views.details, name='details'),

	# /blog/create/
	url(r'^create/$', views.create, name='create'),

	# /blog/2/edit
	url(r'^(?P<post_id>[0-9]+)/edit/', views.edit, name='edit'),

	# blog/2/delete
	url(r'^(?P<post_id>[0-9]+)/delete/', views.delete, name='delete'),
	
]