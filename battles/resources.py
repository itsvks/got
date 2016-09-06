from import_export import resources, fields

from battles.models import Battle


class BattleResource(resources.ModelResource):

    class Meta:
        model = Battle
