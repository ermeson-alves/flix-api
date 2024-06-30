from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class MovieAdmin(admin.ModelAdmin):
    pass
