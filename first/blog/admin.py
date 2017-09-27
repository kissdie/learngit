
from django.contrib import admin
from .models import Blog, Tag

class BlogAdmin(admin.ModelAdmin):
    list_display = ('tag', 'title', 'author', 'data')
    list_filter = ['data']
    search_fields = ['text']

admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)

# Register your models here.
