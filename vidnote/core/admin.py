from django.contrib import admin
from .models import Video, Note

# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['url', 'processed', 'created_at', 'updated_at']
    list_filter = ['processed', 'created_at']
    search_fields = ['url']
    readonly_fields = ['created_at', 'updated_at']
    
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['video', 'content_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'video__url']
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'

