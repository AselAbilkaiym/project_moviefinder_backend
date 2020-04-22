from django.shortcuts import render

from api.serializers import GenreSerializer, MovieSerializer, ManagerSerializer
from api.models import Genre, Movie, Manager, User

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

@api_view(['GET', 'PUT', 'DELETE'])
def genre(request, id):
    if request.method == 'GET':
        pass

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
            genre = Genre.objects.get(name=request.data['genre'])
            manager = Manager.objects.get(username=request.data['publisher'])
            Movie.objects.create(
                name = request.data['name'],
                image = request.data['image'],
                description = request.data['description'],
                text = request.data['text'],
                publisher = manager,
                genre = genre,
            )
        except:
            return Response({'err': 'genre is invalid'}, status=status.HTTP_404_NOT_FOUND)
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

    def put(self, request, id):
        movie = self.get_movie(id)
        try:
            genre = Genre.objects.get(name=request.data['genre'])
            manager = Manager.objects.get(username=request.data['publisher'])            
        except:
            return Response({"server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        movie.genre = genre
        movie.publisher = manager
        movie.name = request.data['name']
        movie.description = request.data['description']
        movie.text = request.data['text']
        movie.image = request.data['image']
        movie.save()
        return Response({'updated'}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        movie = self.get_movie(id)
        movie.delete()
        return Response({'deleted'}, status=status.HTTP_200_OK)

class ManagerView(APIView):
    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'created'}, status=status.HTTP_200_OK)
        return Response({'err'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)