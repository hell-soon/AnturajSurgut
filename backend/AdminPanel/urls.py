from django.urls import path
from AdminPanel.Views.FeedBackView.FeedBack import test

urlpatterns = [
    path("test/", test, name="test"),
]
