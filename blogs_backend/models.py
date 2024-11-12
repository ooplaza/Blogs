from django.db import models


class AbstractModel(models.Model):
    """Abstract model for common fields"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(AbstractModel):
    """Author model"""

    email = models.EmailField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(AbstractModel):
    """Post model"""

    class StatusChoices(models.TextChoices):
        """Status choices for post"""

        DRAFT = "draft"
        PUBLISHED = "published"

    content = models.TextField()
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default=StatusChoices.DRAFT
    )

    def __str__(self):
        return self.title


class Comment(AbstractModel):
    """Comment model"""

    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.name} - {self.post.title}"
