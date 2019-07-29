from django.contrib import admin
from .models import Blog
from .models import NewBlog

admin.site.register(Blog)
admin.site.register(NewBlog)