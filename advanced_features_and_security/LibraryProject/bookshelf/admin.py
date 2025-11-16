from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


# Custom admin for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add your custom fields here so they appear in admin forms
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )


# Register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
