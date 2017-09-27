# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=200, null=True, verbose_name='\u6807\u7b7e\u5206\u7c7b')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=256, null=True, verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='data',
            field=models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=2562, verbose_name='\u6807\u9898'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(to='blog.Tag', null=True),
        ),
    ]
