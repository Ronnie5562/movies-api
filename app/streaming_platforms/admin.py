"""
Admin configuration for the Streaming Platforms app.
"""
from django.contrib import admin
from streaming_platforms.models import Platform
from django.utils.translation import gettext as translate_text


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    """
    Platform model for admin
    """
    list_display = ['name', 'website']
    search_fields = ['name', 'website']
    readonly_fields = ['date_added', 'date_modified']

    fieldsets = (
        (
            translate_text('Platform Information'),
            {
                'fields': (
                    'name',
                    'about',
                    'website'
                )
            }
        ),
        (
            translate_text('Status Information'),
            {
                'fields': (
                    'date_added',
                    'date_modified'
                )
            }
        )
    )
