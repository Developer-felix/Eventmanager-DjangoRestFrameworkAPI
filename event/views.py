from django.shortcuts import render
from event.models import Event
from event.serializers import EventSerializer
from rest_framework import viewsets

class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer