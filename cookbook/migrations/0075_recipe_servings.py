# Generated by Django 3.0.7 on 2020-08-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0074_remove_keyword_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1),
        ),
    ]
