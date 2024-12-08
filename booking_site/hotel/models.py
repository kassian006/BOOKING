from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


STATUS_CHOICES =(
    ('customer', 'customer'),
    ('owner', 'owner')
)

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(16),
                                                       MaxValueValidator(80)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='customer')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=40)
    country = models.CharField(max_length=32)
    owner = models.CharField(max_length=32)
    city = models.CharField(max_length=16)
    description = models.TextField()
    address = models.CharField(max_length=32)
    hotel_video = models.FileField(upload_to='hotel_video/')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(6)], verbose_name='Рейтинг')
    breakfast = models.BooleanField(default=True, verbose_name="Хороший завтрак")
    restaurant = models.BooleanField(default=True, verbose_name="Ресторан")
    parking = models.BooleanField(default=False, verbose_name="Парковка")
    fitness = models.BooleanField(default=False, verbose_name='Фитнес-центр')

    def __str__(self):
        return (f'{self.hotel_name} - {self.country} - {self.breakfast} - {self.parking} - {self.restaurant} - {self.fitness} '
                f' - {self.city} - {self.owner}')


    def get_avg_rating(self):
        ratings = self.comments.all()
        if ratings.exists():
            return round(sum(i.stars for i in ratings) / ratings.count(), 1)
        return 0


class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel', on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return f'{self.hotel_image}'


class Room(models.Model):
    room_number = models.IntegerField()
    hotel_room = models.ForeignKey(Hotel, related_name='hotel_room', on_delete=models.CASCADE)
    ROOM_CHOICES = (
        ('free', 'free'),
        ('booked', 'booked'),
        ('busy', 'busy')
    )
    room_class = models.CharField(choices=ROOM_CHOICES, max_length=16)
    TYPE_CHOICES = (
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=32)
    room_price = models.PositiveIntegerField()
    room_description = models.TextField()
    all_inclusive = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_number} - {self.type} - {self.hotel_room}'


class RoomPhotos(models.Model):
    room = models.ForeignKey(Room, related_name='photos', on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return f'{self.room_image}'


class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    stars = models.IntegerField(choices=[(i, str(i))for i in range(1, 6)], null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.user_name},{ self.hotel} - {self.stars}'

