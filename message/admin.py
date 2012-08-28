#coding=utf-8
from django.contrib import admin
from myblog.message.models import *

class MessageAdmin(admin.ModelAdmin):  
        list_display = ('title','name','email','content','time',"reply","replytime")



admin.site.register(Message,MessageAdmin)

