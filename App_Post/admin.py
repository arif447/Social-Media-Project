from django.contrib import admin
from App_Post.models import Post,Like

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'caption', 'image',  'date', 'update_date']

    class Meta:
        model = Post

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
