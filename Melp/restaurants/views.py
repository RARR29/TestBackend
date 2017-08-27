from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer, StaticsSerializer
from rest_framework.decorators import list_route
from rest_framework.response import Response
from geopy.distance import vincenty
from statistics import stdev

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @list_route(methods=['GET'], )
    def statistics(self, request):
        ser = StaticsSerializer(data=self.request.query_params)
        ser.is_valid(raise_exception=True)

        lat = ser.validated_data.get('latitude')
        lng = ser.validated_data.get('longitude')
        radio = ser.validated_data.get('radius')

        allRestaurant = Restaurant.objects.all()
        centro = (lat,lng)
        total_restaurants = 0
        suma_ratings = 0
        all_ratings = []
        avg = None
        std = None
        for oneRestaurant in allRestaurant:
            punto = (oneRestaurant.lat,oneRestaurant.lng)
            d = self.calcular_distancia_geografica(centro,punto)
            if d < radio:
                suma_ratings += oneRestaurant.rating
                total_restaurants += 1
                all_ratings.append(oneRestaurant.rating)
        resp = {}
        resp['count'] = total_restaurants

        if total_restaurants > 0:
            avg = round(suma_ratings / total_restaurants,5)
            std = round(stdev(all_ratings),5)
        resp['avg'] = avg
        resp['std'] = std


        return Response(resp)

    def calcular_distancia_geografica(self,centro,punto):
        distancia = vincenty(centro, punto).meters
        return distancia