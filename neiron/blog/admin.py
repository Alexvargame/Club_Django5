from django.contrib import admin
from .models import Category, Tag, Article, Comment, Reaction



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tag)
class tagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Comment)
admin.site.register(Reaction)
