from rest_framework import serializers
from api.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'id', 'name'
        
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    image = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    genre = GenreSerializer()