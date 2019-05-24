from rest_framework.routers import SimpleRouter,DefaultRouter

from booktest.views import BookInfoViewSet

urlpatterns = [

]

# router = SimpleRouter()
router = DefaultRouter()
router.register(r"books", BookInfoViewSet, "books")

urlpatterns += router.urls