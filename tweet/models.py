import uuid
from django.contrib.auth.models import User
from django.db import models


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tweet_like'


class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    likes = models.ManyToManyField(User, related_name='tweet_like', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True, verbose_name='content')
    image = models.FileField(upload_to='images/', blank=True, null=True, verbose_name='image')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='date_time_created')

    class Meta:
        db_table = 'tweet'
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'
        ordering = ['-timestamp']

    def __str__(self):
        return self.content

    @property
    def is_retweet(self):
        return self.parent is not None

    # def get_absolute_url(self):
    #     return reverse("article_detail", args=[str(self.id)])
