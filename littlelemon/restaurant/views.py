from django.shortcuts import render
from rest_framework import generics
from .serializers import BookingSerializer , MenuSerializer
from .models import Booking , Menu
from rest_framework import viewsets
from rest_framework import permissions
class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [permissions.IsAuthenticated]