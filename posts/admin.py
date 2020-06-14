from django.contrib import admin
from .models import post,category,post_author,comments
# Register your models here.

admin.site.register(post_author)
admin.site.register(post)
admin.site.register(category)
admin.site.register(comments)

