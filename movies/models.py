from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField(null=True, blank=True)
    resume = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(
                Genre,
                on_delete=models.PROTECT,
                related_name='movies' # permite saber todos os filmes de determinado gênero ao fazer query de genero
            )
    actors = models.ManyToManyField(
                Actor,
                related_name='movies' # permite saber todos os filmes que um ator participa ao fazer query de ator
            )

    def __str__(self):
        return self.title
