# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^essays/$', views.EssaysPageView.as_view(), name='essays'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='projects'),
    url(r'^projects/(?P<pk>\d+)$',
        views.ProjectDetailView.as_view(), name='project-detail'
        ),
    url(r'^essays/view/(?P<slug>[^\.]+).html', 
        views.view_post, 
        name='view_blog_post'),
    url(r'^essays/category/(?P<slug>[^\.]+).html', 
        views.view_category, 
        name='view_blog_category'),
]



