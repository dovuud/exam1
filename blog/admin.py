from django.contrib import admin
from .models import Category,Tag,Author,Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'author')
    list_display_links= ('id', 'title', 'category', 'author')
    filter_horizontal = ('tags',)
    search_fields = ('title', 'category', 'author')


admin.register(Category)
admin.register(Tag)
admin.register(Author)
admin.register(Post, PostAdmin)
