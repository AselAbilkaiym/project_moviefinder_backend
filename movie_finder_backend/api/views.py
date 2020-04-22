from django.shortcuts import render

from api.serializers import GenreSerializer, MovieSerializer
from api.models import Genre, Movie

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
import json

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
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"created"}, status=status.HTTP_200_OK)
        return Response({"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def movie_by_genre(request, id):
    try:
        genre = Genre.objects.get(id=id)
        movies = genre.movie_set.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MovieList(APIView):
    def get(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'err'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            genre = Genre.objects.get(id=request.data['genre']['id'])
        except:
            return Response({'err': 'genre is invalid'}, status=status.HTTP_404_NOT_FOUND)
        
        Movie.objects.create([
    {
        "id": 1,
        "name": "genre1"
    },
    {
        "id": 2,
        "name": "genre2"
    }
]
            name = request.data['name'],
            image = request.data['image'],
            description = request.data['description'],
            text = request.data['text'],
            genre = genre
        )
        
        return Response({"created"}, status=status.HTTP_200_OK)


class MovieDetailed(APIView):
    permission_classes = (IsAuthenticated, )

    def get_movie(self, id):
        try:
            return Movie.objects.get(id=id)
        except:
            return Response({"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        movie = self.get_movie(id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)