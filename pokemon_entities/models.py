from django.db import models  # noqa F401


class Pokemon(models.Model):
    """Покемон и его краткое описание."""
    title = models.CharField(
        max_length=200, verbose_name="Покемон"
    )
    image = models.ImageField(
        null=True, upload_to="Image", verbose_name="Изображение"
    )
    description = models.TextField(
        blank=True, verbose_name="Описание"
    )
    title_en = models.CharField(
        max_length=200, blank=True, verbose_name="Покемон(english)"
    )
    title_jp = models.CharField(
        max_length=200, blank=True, verbose_name="Покемон(japan)"
    )
    evolution_from = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.SET_NULL,
        related_name="evolution_to", verbose_name="Эволюция из кого "
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Характеристика покемона"""
    pokemon = models.ForeignKey(
        Pokemon, null=True, on_delete=models.SET_NULL,
        verbose_name="Покемон", related_name="entities"
    )
    lat = models.FloatField(
        null=True, verbose_name="Широта"
    )
    lon = models.FloatField(
        null=True, verbose_name="Долгота"
    )
    appeared_at = models.DateTimeField(
        null=True, verbose_name="Появится"
    )
    disappeared_at = models.DateTimeField(
        null=True, verbose_name="Исчезнет"
    )
    level = models.IntegerField(
        null=True, blank=True, verbose_name="Уровень"
    )
    health = models.IntegerField(
        null=True, blank=True, verbose_name="Здоровье"
    )
    strength = models.IntegerField(
        null=True, blank=True, verbose_name="Сила"
    )
    defence = models.IntegerField(
        null=True, blank=True, verbose_name="Защита"
    )
    stamina = models.IntegerField(
        null=True, blank=True, verbose_name="Выносливость"
    )

    def __str__(self):
        return "{},{}".format(self.pokemon.title, self.level)
