"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('$/',views.post_list_view),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list_view,name='post_list_by_tag_name'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail_view,name='post_detail'),
    re_path(r'^(?P<id>\d+)/share/$',views.mail_send_view),

    #path('(?P<year>d{4})/(?P<month>[a-z]{3})/(?P<day>w{1,2})/(?P<slug>[-w]+)/$',views.post_detail_view,name='post_detail'),
    #path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail_view,name='post_detail'),
]
