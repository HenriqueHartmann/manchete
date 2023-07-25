from django.contrib import admin

from app_news.models.News import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    empty_value_display = ''
    list_filter = ('title', 'created_by__email')
    search_fields = ('title', 'created_by__email')
    list_per_page = 25
    ordering = ['-created_at'] 

admin.site.register(News, NewsAdmin)
