from django.contrib import admin
from core.account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'fullname', 'is_active', 'last_login', 'created_at')
    list_display_links = ('email', )
    search_fields = ('fullname', 'username', )
    ordering = ('-created_at', )
