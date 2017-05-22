from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from games_review import views

app_name = 'games_review'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jeu/(?P<slug>[\w-]+)/$', views.game, name='game'),
    url('^', include('django.contrib.auth.urls'))
]
