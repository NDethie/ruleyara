from django.urls import path
from . import views
from django.conf.urls import include, url


urlpatterns = [
    url(r'^addrules/$', views.AddRules),
    url(r'^$', views.Index),
    url(r'^search/$', views.Search),
    url(r'^tags/$', views.AddTags),
    url(r'^taging/$', views.Taging),
    url(r'^upload/$', views.Upload),

    

]
