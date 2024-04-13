"""
Admin configuration for the casts app.
"""
from django.contrib import admin
from django.utils.translation import gettext as translate_text
from casts.models import Cast, Award, AwardReceived


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    """
    The Cast model for admin
    """
    fieldsets = (
        (
            translate_text('Personal Information'),
            {
                'fields': (
                    'name',
                    'well_known_as',
                    'age',
                    'gender',
                    'bio',
                )
            }
        ),
        (
            translate_text('Career Information'),
            {
                'fields': (
                    'role',
                )
            }
        ),
    )


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    """
    The Award model for admin
    """
    fieldsets = (
        (
            translate_text('Award Information'),
            {
                'fields': (
                    'name',
                    'category',
                    'description',
                )
            }
        ),
    )


@admin.register(AwardReceived)
class AwardReceivedAdmin(admin.ModelAdmin):
    """
    The AwardReceived model for admin
    """
    fieldsets = (
        (
            translate_text('Award Information'),
            {
                'fields': (
                    'recipient',
                    'award',
                    'year_received',
                )
            }
        ),
    )
