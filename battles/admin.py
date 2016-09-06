from django.contrib import admin
from import_export.admin import ImportExportMixin

from battles.models import Battle
from battles.resources import BattleResource


class BattleAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = BattleResource
    list_display = ('id', 'name', 'year', 'location', 'battle_type')


admin.site.register(Battle, BattleAdmin)
