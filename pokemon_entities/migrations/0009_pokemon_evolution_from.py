# Generated by Django 4.1.7 on 2023-03-26 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_pokemon_title_en_pokemon_title_jp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='evolution_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemon'),
        ),
    ]
