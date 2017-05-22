# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 17:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games_review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Jeu', 'verbose_name_plural': 'Jeux'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Categorie', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='games_review.Game'),
        ),
    ]
