# tictactoe/urls.py

from django.urls import path
from .views import game_view,make_move,tictactoe
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<int:game_id>/', game_view, name='game_view'),
    path('<int:game_id>/make_move/<int:position>/', make_move, name='make_move'),
    path('',tictactoe,name='tictactoe'),
]
