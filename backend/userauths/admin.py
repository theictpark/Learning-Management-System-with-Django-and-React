from django.contrib import admin
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'full_name', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'full_name')
    ordering = ('email',)
    list_filter = ('is_staff', 'is_active') 

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'date')
    search_fields = ('user__email', 'full_name')
    ordering = ('-date',)
    list_filter = ('date',)
