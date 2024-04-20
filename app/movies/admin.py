"""
Admin configuration for the movies app.
"""
from movies import models
from casts.models import Cast
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as translate_text


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    The Genre model for admin
    """
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    readonly_fields = ['date_added', 'date_modified']

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'description'
                )
            }
        ),
        (
            translate_text('Status Information'),
            {
                'fields': (
                    'is_active',
                    'date_added',
                    'date_modified'
                )
            }
        )
    )


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    The Movie model for admin
    """
    list_display = ['title', 'year', 'duration', 'bbfc_rating', 'avg_rating']
    search_fields = ['title', 'year', 'duration', 'bbfc_rating']
    readonly_fields = [
        'date_added', 'date_modified',
        'avg_rating', 'rating_count', 'popularity'
    ]
    filter_horizontal = ['actors', 'directors', 'starring', 'genres']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "actors":
            kwargs["queryset"] = Cast.objects.filter(role='actor')
        elif db_field.name == "directors":
            kwargs["queryset"] = Cast.objects.filter(role='director')
        if db_field.name == "starring":
            kwargs["queryset"] = Cast.objects.filter(role='actor')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    fieldsets = (
        (
            translate_text('Movie Information'),
            {
                'fields': (
                    'title',
                    'intro',
                    'storyline',
                    'year',
                    'duration',
                    'genres'
                )
            }
        ),
        (
            translate_text('Classification'),
            {
                'fields': (
                    'content_type',
                    'bbfc_rating'
                )
            }
        ),
        (
            translate_text('Rating Information'),
            {
                'fields': (
                    'avg_rating',
                    'rating_count',
                    'popularity'
                )
            }
        ),
        (
            translate_text('Cast Information'),
            {
                'fields': (
                    'actors',
                    'starring',
                    'directors'
                )
            }
        ),
        (
            translate_text('Platform Information'),
            {
                'fields': (
                    'platform',
                )
            }
        ),
        (
            translate_text('Status Information'),
            {
                'fields': (
                    'is_active',
                    'date_added',
                    'date_modified'
                )
            }
        )
    )


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    """
    The Season model for admin
    """
    list_display = ['title', 'duration', 'movie', 'avg_rating']
    search_fields = ['title', 'duration', 'movie']
    readonly_fields = [
        'date_added', 'date_modified',
        'avg_rating', 'rating_count', 'popularity'
    ]

    fieldsets = (
        (
            translate_text('Season Information'),
            {
                'fields': (
                    'title',
                    'intro',
                    'storyline',
                    'duration',
                    'movie'
                )
            }
        ),
        (
            translate_text('Rating Information'),
            {
                'fields': (
                    'avg_rating',
                    'rating_count',
                    'popularity'
                )
            }
        ),
        (
            translate_text('Views Information'),
            {
                'fields': (
                    'views',
                )
            }
        ),
        (
            translate_text('Status Information'),
            {
                'fields': (
                    'is_active',
                    'date_added',
                    'date_modified'
                )
            }
        )
    )


@admin.register(models.Episode)
class EpisodeAdmin(admin.ModelAdmin):
    """
    The Episode model for admin
    """
    list_display = ['title', 'duration', 'season', 'avg_rating']
    search_fields = ['title', 'duration', 'season']
    readonly_fields = [
        'date_added', 'date_modified',
        'avg_rating', 'rating_count', 'popularity'
    ]

    fieldsets = (
        (
            translate_text('Season Information'),
            {
                'fields': (
                    'title',
                    'intro',
                    'storyline',
                    'duration',
                    'season'
                )
            }
        ),
        (
            translate_text('Rating Information'),
            {
                'fields': (
                    'avg_rating',
                    'rating_count',
                    'popularity'
                )
            }
        ),
        (
            translate_text('Views Information'),
            {
                'fields': (
                    'views',
                )
            }
        ),
        (
            translate_text('Status Information'),
            {
                'fields': (
                    'is_active',
                    'date_added',
                    'date_modified'
                )
            }
        )
    )


@admin.register(models.ContentView)
class ContentViewAdmin(admin.ModelAdmin):
    """
    The ContentView model for admin
    """
    list_display = ['content_type', 'object_id', 'viewed_by', 'viewed_at']
    readonly_fields = ['content_type', 'object_id', 'viewed_by', 'viewed_at']

    fieldsets = (
        (
            translate_text('Content Information'),
            {
                'fields': (
                    'content_type',
                    'object_id',
                )
            }
        ),
        (
            translate_text('Viewer Information'),
            {
                'fields': (
                    'viewed_by',
                    'viewed_at'
                )
            }
        )
    )


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for managing reviews.
    """
    list_display = ['author', 'content_type',
                    'object_id', 'rating', 'is_active']
    search_fields = ['author', 'content_type',
                     'object_id', 'rating', 'is_active']
    readonly_fields = ['date_added', 'date_modified']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "content_type":
            kwargs["queryset"] = ContentType.objects.filter(
                model__in=['movie', 'season', 'episode'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        (
            translate_text('Review Information'),
            {
                'fields': (
                    'author',
                    'content_type',
                    'object_id',
                    'rating',
                    'comment'
                )
            }
        ),
        (
            translate_text('Status Information'),
            {
                'fields': (
                    'is_active',
                    'date_added',
                    'date_modified'
                )
            }
        )
    )
