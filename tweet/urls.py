from django.urls import path
from .views import *

app_name = 'tweet'

urlpatterns = [
    path('detail/<uuid:tweet_id>', tweet_detail_view, name='tweet_detail'),
    path('delete/<uuid:tweet_id>', tweet_delete_view, name='tweet_delete'),
    path('list/', tweet_list_view, name='list'),
    path('create/', tweet_create_view, name='create'),
    path('action/', tweet_action_view, name='action')
]
