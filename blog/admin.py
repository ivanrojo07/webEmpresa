from django.contrib import admin
from .models import Category, Post
from django.utils.safestring import mark_safe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'published_at', 'post_categories')
    ordering=('author',)
    search_fields=('title','author__username', 'categories__name')
    date_hierarchy='published_at'
    list_filter=('categories__name','author__username')

    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

    def imagen(self,obj):
        return mark_safe('<image style:"height=15px; width=15px;" src="%s" />'%obj.image.url)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
