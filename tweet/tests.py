from django.test import TestCase
from .models import Tweet
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abc', password='somepassword')
        Tweet.objects.create(content='my 1st tweet', user=self.user)

    def test_user_created(self):
        tweet = Tweet.objects.create(content='my 2nd tweet', user=self.user)
        self.assertEqual(tweet.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_action_like(self):
        client = self.get_client()
        tweet = Tweet.objects.all().first()
        response = client.post('/api/tweet/action/', {'id': tweet.id, 'action': 'like'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['likes'], 1)

    def test_action_unlike(self):
        client = self.get_client()
        tweet = Tweet.objects.all().first()
        response = client.post('/api/tweet/action/', {'id': tweet.id, 'action': 'unlike'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['likes'], 0)

    def test_action_retweet(self):
        client = self.get_client()
        tweet = Tweet.objects.all().first()
        response = client.post('/api/tweet/action/', {'id': tweet.id, 'action': 'retweet'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('parent').get('content'), tweet.content)
        data = response.json()
        self.assertNotEqual(tweet.id, data.get('id'))
