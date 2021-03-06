#coding=utf-8
from django.contrib import admin
from myblog.blog.models import *

#######################用于生成为文章添加图片的模块，其实就是在ArticleAdmin的后台模块中相关连上ArticPic，以便于能够方便的复制图片链接
class MediaAdmin(admin.StackedInline):
	  model = ArticlePic

#######################本想依葫芦画瓢，将留言与文章一同在后台整合，但是该做法并不奏效
#class ReplyAdmin(admin.StackedInline):
#	  model = Comment


class ArticleAdmin(admin.ModelAdmin):  
        list_display = ('id','title','time','type')
        ###########导入富文本编辑框的js脚本
        class Media:
             js=('/site_media/js/tiny_mce/tiny_mce.js','/site_media/js/textareas.js')  
        #############用于生成为文章添加图片的模块               
        inlines = [MediaAdmin,]   
        
        #####inlines = [ReplyAdmin,]       


class ArticlePicAdmin(admin.ModelAdmin):  
        list_display = ('title','article')


class CommentAdmin(admin.ModelAdmin):  
        list_display = ('title','name','email','article','content','time',"reply","replytime")    ##########这里自定义的是在后台管理处所显示的数据项信息




#####################需要哪些数据表在后台管理里显示，可以在这里自定义

admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleType)
admin.site.register(ArticlePic,ArticlePicAdmin)
admin.site.register(Comment,CommentAdmin)




