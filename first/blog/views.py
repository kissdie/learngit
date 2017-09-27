from django.shortcuts import render
from .models import Tag, Blog


def index(request):
    article = Blog.objects.all()
    tag = Tag.objects.all()
    dict = {'tags': tag, 'articles': article}
    return render(request, "blog.html", dict)


def list(request, tag_tag):
    article = Blog.objects.filter(tag__tag=tag_tag)
    return render(request, 'Tag_detail.html', {"articles": article})


def detail(request, a_id):
    article_detail = Blog.objects.get(pk=a_id)
    return render(request, 'artile_detail.html', {'article_detail': article_detail})




