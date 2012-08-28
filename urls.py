#coding=utf-8

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from myblog import settings
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/(?P<object_id>\d+)$', 'myblog.blog.views.Archive_Blog'),   ######### 用于实现分页  注意这里的(?P<object_id>\d+)!!!!!!!  以及后面的$   符号!!!!!!!!!
	(r'^blog/$', 'myblog.blog.views.Paginate_Blog'),	               ########## 用于实现分页  注意这里的  $   符号!!!!!!!!!
    (r'^message/$', 'myblog.message.views.Message_Index'),
    #主页
    #(r'^$',direct_to_template,{'template':'index.html'}),
    (r'^$', 'myblog.message.views.ContactMe_Index'),
    #仅提供给主页使用的静态文件，以static作为匹配标记
	('^static/(?P<path>.*)','django.views.static.serve',{'document_root':settings.current_dir + '/static'}),
	(r'^photo/(?P<path>.*)','django.views.static.serve',{'document_root':settings.current_dir + '/media/photo'}),
	######Tinymce
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',    {'document_root': 'media'})


    
)
