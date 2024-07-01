# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import TicTacToe

def tictactoe(request):
    return render(request, 'tictactoe/tictactoe.html')


# tictactoe/views.py

def game_view(request, game_id):
    game = get_object_or_404(TicTacToe, pk=game_id)
    return render(request, 'tictactoe/tictactoe.html', {'game': game})


def make_move(request, game_id, position):
    game = get_object_or_404(TicTacToe, pk=game_id)
    game.make_move(int(position))
    print("estoy en views")
    # Lógica para determinar el ganador
    winner = game.get_winner()

    if winner or game.is_draw():
        return redirect('game_view', game_id=game_id)

    return redirect('game_view', game_id=game_id)
