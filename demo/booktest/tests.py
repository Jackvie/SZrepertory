# from django.test import TestCase

# Create your tests here.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
import django
django.setup()
from rest_framework.routers import SimpleRouter
from booktest.views import BookInfoViewSet

urlpatterns = [

]

router = SimpleRouter()
router.register(r"books", BookInfoViewSet, "books")

for url in router.urls:
    print(url)


# urlpatterns += router.urls


