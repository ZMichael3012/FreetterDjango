# Generated by Django 4.0.3 on 2022-04-04 05:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'verbose_name': 'Tweet', 'verbose_name_plural': 'Tweets'},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
