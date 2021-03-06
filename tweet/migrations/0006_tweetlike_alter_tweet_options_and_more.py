# Generated by Django 4.0.3 on 2022-04-08 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0005_alter_tweet_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tweet_like',
            },
        ),
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Tweet', 'verbose_name_plural': 'Tweets'},
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='date_time_created',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_like', through='tweet.TweetLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.tweet'),
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
