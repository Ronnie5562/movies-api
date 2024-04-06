"""
Admin site configuration
"""

from django.contrib import admin
from core import models
from django.utils.translation import gettext as translate_text
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    """
    The user model for admin
    """
    ordering = ['id']
    list_display = ['id', 'email', 'name', 'is_active', 'is_staff']
    readonly_fields = ['last_login']
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password'
                )
            }
        ),
        (
            translate_text('Personal Info'),
            {
                'fields': (
                    'name',
                )
            }
        ),
        (
            translate_text('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (
            translate_text('Important dates'),
            {
                'fields': (
                    'last_login',
                )
            }
        )
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
    )


admin.site.register(models.User, UserAdmin)