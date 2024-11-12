from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from blogs_backend.models import Author, Post, Comment
from rest_framework import viewsets
from blogs_backend.serializers import (
    PostSerializer,
    CommentSerializer,
    AuthorSerializer
)


class PostListView(viewsets.GenericViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post"]

    def create(self, request, *args, **kwargs):
        """Create a post instance."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """Return all posts with certain filtering status."""
        name = self.request.query_params.get("name")
        published_date = self.request.query_params.get("published_date")

        if name and published_date:
            return Post.objects.filter(
                author__name=name,
                created_at__date=published_date
            )

        return Post.objects.all()

    def list(self, request, *args, **kwargs):
        """List all posts."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a post instance."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentListView(viewsets.GenericViewSet):
    """
    A viewset for viewing and editing comment instances.
    """
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post"]

    def create(self, request, *args, **kwargs):
        """Create a comment instance."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
