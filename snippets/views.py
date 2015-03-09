from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):

    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
