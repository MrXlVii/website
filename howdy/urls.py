# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = 'home'),
    url(r'^about/$', views.AboutPageView.as_view(), name = 'about'),
    url(r'^essays/$', views.EssaysPageView.as_view(), name = 'essays'),
    url(r'^projects/$', views.ProjectsPageView.as_view(), name = 'projects'),
]
