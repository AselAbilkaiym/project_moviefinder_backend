from django.shortcuts import render

from api.serializers import GenreSerializer, MovieSerializer
from api.models import Genre, Movie

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def test(request):
    return Response({"hello"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def genres(request):
    if request.method == 'GET':
        try:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def movie_by_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
        movies = genre.movie_set.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


