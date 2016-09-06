import django_filters

from battles.models import Battle


class BattleFilter(django_filters.FilterSet):
    class Meta:
        model = Battle
        fields = ['name', 'attacker_king', 'defender_king', 'battle_type', 'location', 'year']