from rest_framework import generics
from tweet.models import Tweet
from .serializers import TweetSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsTweetAuthorOrReadOnly


from django.contrib.auth import authenticate


class UserCreate(APIView):

    authentication_classes = ()
    # model = get_user_model
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(
        self,
        request,
    ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                {
                    "token": user.auth_token.key,
                    "user": user.username,
                }
            )

        else:
            return Response(
                {"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )


class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsTweetAuthorOrReadOnly,
    ]  # new
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
