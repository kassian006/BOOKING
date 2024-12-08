
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotel_description_en_hotel_description_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_class_en',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_class_ru',
        ),
    ]
