from django.shortcuts import render, get_object_or_404
from games_review.models import *
from django.core.paginator import *


# Create your views here.
def index(request):
    if request.GET.get('search_games'):
        game_list = Game.objects.filter(name__icontains=request.GET.get('search_games'))
    else:
        game_list = Game.objects.all()
    paginator = Paginator(game_list, 7)

    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'games': games, 'INDEX_PAGE_TITLE': 'Les jeux'})


def game(request, slug):
    game = get_object_or_404(Game, slug=slug)

    if request.POST.get('new_comment'):

        game.comments.add(request.POST.get('new_comment'))

    comments = game.comments.all()
    return render(request, 'game.html', {'game': game, 'comments': comments})
