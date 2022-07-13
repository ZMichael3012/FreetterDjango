from Freetter.rest_api.dev import DevAuthentication
from .models import Tweet
from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([SessionAuthentication, DevAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    queryset = Tweet.objects.filter(id=tweet_id)
    if not queryset.exists():
        return Response({}, status=404)
    obj = queryset.first()
    serializer = TweetSerializer(obj)

    return Response(serializer.data, status=200)


@api_view(['DELETE', 'POST'])
@authentication_classes([SessionAuthentication, DevAuthentication])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    queryset = Tweet.objects.filter(id=tweet_id)
    if not queryset.exists():
        return Response({}, status=404)

    queryset = queryset.filter(user=request.user)
    if not queryset.exists():
        return Response({'message': 'You cannot delete this tweet.'}, status=404)

    obj = queryset.first()
    obj.delete()

    return Response({'message': 'Tweet was deleted.'}, status=200)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, DevAuthentication])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        action = data.get('action')
        content = data.get('content')

        queryset = Tweet.objects.filter(id=tweet_id)
        if not queryset.exists():
            return Response({}, status=404)

        obj = queryset.first()
        if action == 'unlike':
            obj.likes.remove(request.user)
            tweet_unlike_serializer = TweetSerializer(obj)
            return Response(tweet_unlike_serializer.data, status=200)
        elif action == 'like':
            obj.likes.add(request.user)
            tweet_like_serializer = TweetSerializer(obj)
            return Response(tweet_like_serializer.data, status=200)
        elif action == 'retweet':
            parent_obj = obj
            new_tweet = Tweet.objects.create(user=request.user, parent=parent_obj, content=content)
            retweet_serializer = TweetSerializer(new_tweet)
            return Response(retweet_serializer.data, status=201)

    return Response({}, status=200)


@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    queryset = Tweet.objects.all()
    username = request.GET.get('username')
    if username:
        queryset = queryset.filter(user__username__iexact=username)

    serializer = TweetSerializer(queryset, many=True)

    return Response(serializer.data, status=200)
