from rest_framework import serializers
from actors.models import Actor
from datetime import date


class ActorModelSerializer(serializers.ModelSerializer):

    class Meta: # informar model e cmapos
        model = Actor
        fields = '__all__'

    def validate_birthday(self, value):
        current_date = date.today()
        try:
            years_ago_18 = current_date.replace(year=current_date.year - 18)
            years_ago_70 = current_date.replace(year=current_date.year - 70)
        except: # special case for February 28th
            years_ago_18 = current_date.replace(year=current_date.year - 18, day=28)
            years_ago_70 = current_date.replace(year=current_date.year - 70, day=28)

        if value > years_ago_18 or value < years_ago_70:
            raise serializers.ValidationError(
                f'O ator a ser cadastrado deve ter entre 18 e 70 anos!'
            )

        return value