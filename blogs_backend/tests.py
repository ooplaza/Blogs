from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blogs_backend.models import Author, Post, Comment


class PostTestCases(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.post_url = reverse("post-list")
        self.comment_url = reverse("comment-list")
        self.author = Author.objects.create(
            name="Test Author",
            email="test_author@example.com",
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post",
            status=Post.StatusChoices.PUBLISHED,
            author=self.author
        )

    def test_create_post(self):
        payload = {
            "title": "Test Post",
            "content": "This is a test post",
            "status": Post.StatusChoices.PUBLISHED,
            "author": self.author.id
        }

        response = self.client.post(self.post_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_a_comment(self):
        payload = {
            "post": self.post.id,
            "author": self.author.id,
            "content": "This is a test comment"
        }

        response = self.client.post(self.comment_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
