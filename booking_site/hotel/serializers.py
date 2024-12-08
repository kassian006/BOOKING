from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учутные данные")


    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'stars']



class HotelPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = ['hotel_image']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel = HotelPhotosSerializer(read_only=True, many=True)
    owner = UserProfileSimpleSerializer()
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'stars', 'owner', 'fitness', 'breakfast', 'restaurant','parking',
                  'description', 'address', 'hotel', 'hotel_video']


class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    photos = RoomPhotosSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['room_number', 'room_price', 'type', 'photos', 'all_inclusive']


# class RoomPhotosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RoomPhotos
#         fields = ['room_image']


class RoomDetailSerializer(serializers.ModelSerializer):
    photos = RoomPhotosSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['room_number', 'hotel_room', 'room_price', 'type', 'photos', 'all_inclusive', 'room_description']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user', 'room', 'check_in', 'check_out', 'status', 'created_at', 'canceled_at']