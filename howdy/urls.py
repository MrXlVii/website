# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^essays/$', views.post_list, name='essays'),
    url(r'^essays/view/(?P<slug>[^\.]+).html', 
        views.view_post, 
        name='view_blog_post'),
    url(r'^essays/category/(?P<slug>[^\.]+).html', 
        views.view_category, 
        name='view_blog_category'),
    url(r'^post/(?P<pk>\d+)/$',
        views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit,
        name='post_edit'),
    url(r'^projects/$', views.project_list, name='projects'),
    url(r'^post/(?P<pk>\d+)/$',
        views.post_detail, name='post_detail'),
]



