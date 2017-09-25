# coding:utf-8
from django.db import models

# Create your models here.

class blog(models.Model):
    #tag = models.CharField(u"分类", max_length=256)
    title = models.CharField(u"标题", max_length=256)
    text = models.TextField(u'内容')
    data = models.DateTimeField(u"发布时间", auto_now_add=True, editable=True)


    def __unicode__(self):
        return self.title

