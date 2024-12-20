# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Number of items per page
}
from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer
from rest_framework import filters
from django_filters import rest_framework as django_filters

class PassengerFilter(django_filters.FilterSet):
    flight = django_filters.NumberFilter(field_name="flight__id", lookup_expr='exact')

    class Meta:
        model = Passenger
        fields = ['flight']

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
