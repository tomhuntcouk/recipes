# Generated by Django 3.0.7 on 2020-06-25 19:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0059_auto_20200625_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.AlterField(
            model_name='sharelink',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a7a91b2e-ad33-4159-a35e-828a5244ede9')),
        ),
    ]
