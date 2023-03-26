# Generated by Django 4.1.7 on 2023-03-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_appeared_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(null=True),
        ),
    ]
