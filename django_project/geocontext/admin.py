"""Model admin class definitions."""

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from geocontext.models.csr import ContextServiceRegistry
from geocontext.models.cache import ContextCache
from geocontext.models.group import ContextGroup
from geocontext.models.collection import ContextCollection
from geocontext.models.group_services import ContextGroupServices
from geocontext.models.collection_groups import CollectionGroups


class GroupServicesInLine(admin.TabularInline):
    """Inline Admin for ContextGroupServices"""
    model = ContextGroupServices
    sortable_field_name = 'order'
    ordering = ('order', )
    extra = 0


class CollectionGroupsInLine(admin.TabularInline):
    """Inline Admin for CollectionGroups"""
    model = CollectionGroups
    sortable_field_name = 'order'
    ordering = ('order',)
    extra = 0


class CSRAdmin(admin.ModelAdmin):
    """Context Service Registry admin model."""
    list_display = ('key', 'name', 'query_type', 'url')


class CacheAdmin(OSMGeoAdmin):
    """Context Cache admin model."""
    list_display = ('name', 'service_registry', 'value', 'expired_time')


class GroupAdmin(admin.ModelAdmin):
    """Context Group admin model."""
    list_display = ('key', 'name', 'group_type', 'description')
    inlines = [GroupServicesInLine]


class CollectionAdmin(admin.ModelAdmin):
    """Context Collection admin model."""
    list_display = ('key', 'name', 'description')
    inlines = [CollectionGroupsInLine]


admin.site.register(ContextServiceRegistry, CSRAdmin)
admin.site.register(ContextCache, CacheAdmin)
admin.site.register(ContextGroup, GroupAdmin)
admin.site.register(ContextCollection, CollectionAdmin)
