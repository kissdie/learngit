# coding:utf-8
from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(u"标签分类", max_length=200,null=True)

    def __unicode__(self):
        return self.tag


class Blog(models.Model):
    tag = models.ForeignKey(Tag, null=True)
    title = models.CharField(u"标题", max_length=2562)
    author = models.CharField(u"作者", max_length=256, null=True)
    text = models.TextField(u'内容')
    data = models.DateTimeField(u"发布时间")

    def __unicode__(self):
        return self.title

