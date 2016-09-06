from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from battles.filters import BattleFilter
from battles.models import Battle
from battles.serializers import BattleSerializer


class BattleList(generics.ListCreateAPIView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    filter_class = BattleFilter


class BattleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleCount(APIView):

    def get(self, request, format=None):
        battles = Battle.objects.count()
        return Response(battles)

