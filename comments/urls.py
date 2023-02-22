from django.urls import path

from .views import UserCommentView
from .views import commentView


urlpatterns = [
    path('new/', commentView),
]