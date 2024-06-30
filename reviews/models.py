from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator
 

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    comment = models.TextField(null=True, blank=True)
    stars = models.IntegerField(
                validators=[  # validators servem para restringir os valores de campos
                    MinValueValidator(0, 'A quantidade de estrelas deve estar entre 0 e 5!'),
                    MaxValueValidator(5, 'A quantidade de estrelas deve estar entre 0 e 5!')
                ]
            )

    def __str__(self):
        return f'{self.movie}'