from rest_framework import serializers
from api.models import Movie, Genre, User, Manager


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'id', 'name'

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'password'

class ManagerSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return Manager.objects.create(**validated_data)

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    image = serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    genre = GenreSerializer()
    publisher = ManagerSerializer()

