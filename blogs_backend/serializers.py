from rest_framework import serializers
from blogs_backend.models import Author, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "email"
        ]


class PostSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(source="created_at", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "published_date",
            "updated_at"
        ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "content",
            "created_at",
            "updated_at"
        ]
