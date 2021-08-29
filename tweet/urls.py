from django.urls import path
from .views import TweetList, TweetDetail, UserCreate, LoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path("tweets/new", TweetCreate.as_view()),
    path("tweets/", TweetList.as_view()),
    path("tweets/<int:pk>/", TweetDetail.as_view()),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("get-auth-token/", obtain_auth_token, name="get_auth_token"),
]
