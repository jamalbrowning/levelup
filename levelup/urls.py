from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views.game_type import GameTypesViewSet
from levelupapi.views.game import  GamesViewSet
from levelupapi.views.event import EventsViewSet
from levelupapi.views.profile import ProfileViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypesViewSet, 'gametype')
router.register(r'games', GamesViewSet, 'game')
router.register(r'events', EventsViewSet, 'event')
router.register(r'profile', ProfileViewSet, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
