from rest_framework import routers
from blogs_backend.views import PostListView, CommentListView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"posts", PostListView, basename="post")
router.register(r"comments", CommentListView, basename="comment")

urlpatterns = router.urls
