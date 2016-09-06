from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from battles import views

urlpatterns = [
    url(r'^$', views.BattleList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BattleDetail.as_view()),
    url(r'^counts/$', views.BattleCount.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
