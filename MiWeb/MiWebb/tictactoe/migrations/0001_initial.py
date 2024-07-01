# Generated by Django 5.0.1 on 2024-01-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicTacToe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(default='         ', max_length=9)),
                ('current_player', models.CharField(default='X', max_length=1)),
            ],
        ),
    ]
