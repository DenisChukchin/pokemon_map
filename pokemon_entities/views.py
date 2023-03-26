import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.utils.timezone import localtime


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entity = PokemonEntity.objects.filter(
        appeared_at__lt=localtime(),
        disappeared_at__gt=localtime()
    )
    for entity in pokemons_entity:
        add_pokemon(
            folium_map,
            entity.lat, entity.lon,
            entity.pokemon.image.path
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemons = Pokemon.objects.get(id=pokemon_id)
        pokemons_info = {
            "pokemon_id": pokemon_id,
            "title_ru": pokemons.title,
            "img_url": pokemons.image.url,
            "description": pokemons.description,
            "title_en": pokemons.title_en,
            "title_jp": pokemons.title_jp
        }
        if pokemons.evolution_from:
            pokemons_info["previous_evolution"] = {
                "title_ru": pokemons.evolution_from.title,
                "pokemon_id": pokemons.evolution_from.id,
                "img_url": pokemons.evolution_from.image.url
            }
        if pokemons.evolution_to.all():
            evolution = pokemons.evolution_to.all().first()
            pokemons_info["next_evolution"] = {
                "title_ru": evolution.title,
                "pokemon_id": evolution.id,
                "img_url": evolution.image.url
            }
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entity = PokemonEntity.objects.filter(
        appeared_at__lt=localtime(),
        disappeared_at__gt=localtime()
    )
    for entity in pokemons_entity:
        add_pokemon(
            folium_map,
            entity.lat, entity.lon,
            entity.pokemon.image.path
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemons_info
    })
