from rest_framework import fields, serializers
from main.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteVacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = []


class FavoriteCvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = []