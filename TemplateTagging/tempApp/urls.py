from django.conf.urls import url
from tempApp import views

app_name = 'tempApp'

urlpatterns = [
     url(r'^relative/$',views.relative,name='relative'),
     url(r'^other/$',views.other,name='other'),
]
