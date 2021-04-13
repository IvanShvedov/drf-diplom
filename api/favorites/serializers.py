from rest_framework import serializers
from main.models import Favorite, Vacancy, Cv
from search.serializers import CvSearchSerializer, VacancySearchSerializer


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteVacancySerializer(serializers.ModelSerializer):

    vacancy = serializers.SerializerMethodField("get_vacancy")

    class Meta:
        model = Favorite
        fields = [
            'user', 'item_id', 'item_type',
            'vacancy'
            ]

    def get_vacancy(self, obj):
        try:
            vacancy = Vacancy.objects.get(id=obj.item_id)
            return VacancySearchSerializer(vacancy, context=self.context).data
        except Vacancy.DoesNotExist:
            return ''


class FavoriteCvSerializer(serializers.ModelSerializer):

    cv = serializers.SerializerMethodField("get_cv")

    class Meta:
        model = Favorite
        fields = [
            'user', 'item_id', 'item_type',
            'cv'
            ]

    def get_cv(self, obj):
        try:
            cv = Cv.objects.get(id=obj.item_id)
            return CvSearchSerializer(cv, context=self.context).data
        except Cv.DoesNotExist:
            return ''