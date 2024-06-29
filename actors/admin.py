from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass # colocando um pass aqui todos os campos são listados em /admin menos o id