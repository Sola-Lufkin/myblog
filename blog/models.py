#coding=utf-8

from django.db import models

# Create your models here.
UPLOAD_TO = 'photo/'

class ArticleType(models.Model):
    type = models.CharField('文章类别',max_length=30,primary_key=True)

    class Meta:
        verbose_name_plural = "文章分类"    

    def __unicode__(self):
        return self.type



class Article(models.Model):
    title = models.CharField('标题',max_length=30)
    time = models.DateTimeField('发表时间') 
    content = models.TextField('文章内容')
    type = models.ForeignKey(ArticleType,verbose_name='文章类别')

    class Meta:
        verbose_name_plural = "博文"   
 
    def __unicode__(self):
        return self.title



class ArticlePic(models.Model):
    title = models.CharField('图片标题',max_length = 120)
    image = models.ImageField('图片',upload_to = UPLOAD_TO)
    article = models.ForeignKey(Article,verbose_name='对应的文章')

    class Meta:
        verbose_name_plural = "博文图片"

    def __unicode__(self):
        describe = u"添加图片请复制后面的路径"
        return '%s:      /%s' % (describe,self.image)


class Comment(models.Model):
    title = models.CharField('留言标题',max_length =30)
    content = models.TextField('留言内容')
    time = models.DateTimeField('发表时间',auto_now_add = True)  #
    name = models.CharField('留言者',max_length=40)
    email = models.EmailField('邮箱',blank=True) 
    reply = models.TextField('回复内容',blank=True)
    replytime = models.DateTimeField('回复时间',blank=True,auto_now = True)  #
    article = models.ForeignKey(Article,verbose_name='对应的文章')

    class Meta:
        verbose_name_plural = "留言"     #######用于在后台列表中显示该功能模块的名称

    def __unicode__(self):
        return u'|- %s -|- %s -|- %s -|- %s -|' % (self.article,self.title,self.time,self.content)      #####用于在后台时描述该数据项


    

