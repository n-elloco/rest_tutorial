from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


class SnippetList(generics.ListCreateAPIView):

    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class SnippetHighlight(generics.GenericAPIView):

    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
