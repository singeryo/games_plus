# encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import ModelForm

class Type(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    def  __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'


class Game(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nom")
    slug = models.SlugField()
    author = models.ForeignKey(User, verbose_name="Auteur")
    release_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()
    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jeu'
        verbose_name_plural = 'Jeux'


class Comment(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, related_name="comments")
    body = models.TextField(max_length=300)
    game = models.ForeignKey(Game, related_name="comments")
    date = models.DateField(auto_now=True, verbose_name="Date")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'
# Create your models here.
