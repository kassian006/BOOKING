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

from .models import *
from rest_framework import viewsets,status,generics
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



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

