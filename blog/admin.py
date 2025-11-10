from django.contrib import admin

from blog.models import Post, Profile, Tag

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Tag)
