# Generated by Django 2.2 on 2019-05-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190505_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luggage',
            name='image',
            field=models.ImageField(blank=True, default='/products_pictures/default.jpg', upload_to='products_pictures'),
        ),
    ]
