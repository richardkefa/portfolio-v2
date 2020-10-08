from django.conf.urls import url
from . import views 

urlpatterns=[
  url('^$',views.recent_projects,name=recentproject)
]