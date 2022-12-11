from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("author", views.AuthorViewSet)
router.register("blogs", views.BlogViewSet)
router.register("categories", views.CategoryViewSet)

urlpatterns = router.urls