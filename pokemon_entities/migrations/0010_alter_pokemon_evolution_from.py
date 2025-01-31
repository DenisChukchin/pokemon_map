# Generated by Django 4.1.7 on 2023-03-26 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_pokemon_evolution_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='evolution_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evolution_to', to='pokemon_entities.pokemon'),
        ),
    ]
