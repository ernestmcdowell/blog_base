from django.contrib import admin

from blog.models import Post, CustomUser, Images, TechStack

# Register your models here.

admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(Images)
admin.site.register(TechStack)
