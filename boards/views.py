from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


def home(request):
    boards=Board.objects.all()
    board_name=list()

    for board in boards:
        board_name.append(board.name)

    response_html='<br>'.join(board_name)
    return HttpResponse(response_html)

# Create your views here.
