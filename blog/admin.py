from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['author__username', 'body']
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'activate']
    list_filter = ['activate', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    actions = ['disable_comment', 'activate_comment']

    @admin.action(description="Desativar Comentários Selecionados")
    def disable_comment(self, request, queryset):
        queryset.update(activate=False)

    @admin.action(description="Ativar Comentários Selecionados")
    def activate_comment(self, reques, queryset):
        queryset.update(activate=True)