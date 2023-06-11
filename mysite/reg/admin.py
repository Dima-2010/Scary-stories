from django.contrib import admin

from reg.models import Articles, Comments, Articles_admin, Post, Video

admin.site.register(Articles)

admin.site.register(Comments)

admin.site.register(Articles_admin)

admin.site.register(Post)

admin.site.register(Video)


