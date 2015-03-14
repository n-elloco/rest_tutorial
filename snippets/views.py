from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):

    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
