from django.contrib import admin
from .models import Like, Post


class TabularInlineLike(admin.TabularInline):
    model = Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at')
    inlines = [TabularInlineLike, ]
