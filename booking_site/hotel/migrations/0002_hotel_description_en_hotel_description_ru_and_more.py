# Generated by Django 5.1.3 on 2024-12-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_name_en',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_name_ru',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_class_en',
            field=models.CharField(choices=[('free', 'free'), ('booked', 'booked'), ('busy', 'busy')], max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_class_ru',
            field=models.CharField(choices=[('free', 'free'), ('booked', 'booked'), ('busy', 'busy')], max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='room_description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_video',
            field=models.FileField(upload_to='hotel_video/'),
        ),
        migrations.AlterField(
            model_name='hotelphotos',
            name='hotel_image',
            field=models.ImageField(upload_to='hotel_images/'),
        ),
        migrations.AlterField(
            model_name='roomphotos',
            name='room_image',
            field=models.ImageField(upload_to='hotel_images/'),
        ),
    ]