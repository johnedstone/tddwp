from django.conf.urls import include, url
# from django.contrib import admin
from lists import views

urlpatterns = [
    url(r'^new', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_lists'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item')
    # url(r'^admin/', include(admin.site.urls)),
]