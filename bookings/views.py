from django.shortcuts import render
from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    
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
    serializer_class = PassengerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PassengerFilter



