# Generated by Django 3.2.8 on 2021-10-17 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonFight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenger_user_id', models.IntegerField(db_index=True)),
                ('challenger_pokemon_id', models.IntegerField(db_index=True)),
                ('challenged_user_id', models.IntegerField(db_index=True)),
                ('challenged_pokemon_id', models.IntegerField(db_index=True)),
                ('challenged_on', models.DateTimeField(default=datetime.datetime.now)),
                ('winner_id', models.IntegerField(db_index=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('accepted', 'accepted'), ('timeout', 'timeout'), ('in_progress', 'in_progress'), ('completed', 'completed')], default='pending', max_length=128)),
            ],
            options={
                'db_table': 'pokemon_fight',
            },
        ),
    ]
