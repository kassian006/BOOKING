from rest_framework.permissions import IsAuthenticated

from . import permissions
from .models import *
from rest_framework import viewsets

from .permissions import  ChekBooking, CheckBookingOwner, ChekReview, ChekRoom, ChekSimpleRoom, ChekRead, CheckCRAD, \
    ChekHotelOwner, CheckCRAD

from .serializers import *
from .filters import HotelFilter, RoomFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset =UserProfile.objects.all()
    serializer_class =UserProfileSerializer


class HotelListViewSet(viewsets.ModelViewSet):
    queryset =Hotel.objects.all()
    serializer_class =HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    ordering_fields = ['stars']
    permission_classes = [CheckCRAD]


class HotelPhotosViewSet(viewsets.ModelViewSet):
    queryset =HotelPhotos.objects.all()
    serializer_class =HotelPhotosSerializer
    permission_classes = [ChekRead]



class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset =Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [CheckCRAD, ChekHotelOwner]


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class =RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['room_number']
    ordering_fields = ['room_price']


class RoomPhotosViewSet(viewsets.ModelViewSet):
    queryset =RoomPhotos.objects.all()
    serializer_class =RoomPhotosSerializer
    permission_classes = [ChekRead]



class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset =Room.objects.all()
    serializer_class =RoomDetailSerializer
    permission_classes = [ChekRoom, ChekSimpleRoom]



class ReviewViewSet(viewsets.ModelViewSet):
    queryset =Review.objects.all()
    serializer_class =ReviewSerializer
    permission_classes = [permissions, ChekReview]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckBookingOwner, ChekBooking]