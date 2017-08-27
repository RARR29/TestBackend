
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from restaurants.views import RestaurantViewSet

router = routers.SimpleRouter()
router.register(r'restaurant', RestaurantViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


urlpatterns += router.urls