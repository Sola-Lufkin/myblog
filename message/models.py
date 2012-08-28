#coding=utf-8

from django.db import models

# Create your models here.


class Message(models.Model):
    title = models.CharField('留言标题',max_length =30)
    content = models.TextField('留言内容')
    time = models.DateTimeField('发表时间',auto_now_add = True)  #
    name = models.CharField('留言者',max_length=40)
    email = models.EmailField('邮箱',blank=True) 
    reply = models.TextField('回复内容',blank=True)
    replytime = models.DateTimeField('回复时间',blank=True,auto_now = True)  #
    

    class Meta:
        verbose_name_plural = "留言板"

    def __unicode__(self):
        return u'|- %s -|- %s -|- %s -|' % (self.title,self.time,self.content)

