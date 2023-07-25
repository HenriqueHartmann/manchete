from django.contrib import admin

from app_auth.models.Profile import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)
    empty_value_display = ''
    list_filter = ('name', 'user__email')
    search_fields = ('name', 'user__email')
    list_per_page = 25
    ordering = ['-created_at'] 

admin.site.register(Profile, ProfileAdmin)
