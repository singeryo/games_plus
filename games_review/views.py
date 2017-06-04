from django.shortcuts import render, get_object_or_404
from games_review.models import *
from django.core.paginator import *
from forms import CommentForm


# Create your views here.
def index(request):
    # Check if requests have been made
    if request.GET.get('search_games'):
        game_list = Game.objects.filter(name__icontains=request.GET.get('search_games'))
    elif request.GET.get('type'):
        type = get_object_or_404(Type, slug=request.GET.get('type'))
        game_list = Game.objects.filter(types=type)
    else:
        game_list = Game.objects.all()

    paginator = Paginator(game_list, 9)

    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'games': games, 'INDEX_PAGE_TITLE': 'Liste des jeux'})


def game(request, slug):
    game = get_object_or_404(Game, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(False)
            comment.game = game
            comment.author = request.user
            comment.save()
    else:
        form = CommentForm()

    comments = game.comments.all()
    return render(request, 'game.html', {'game': game, 'comments': comments, 'form': form})

