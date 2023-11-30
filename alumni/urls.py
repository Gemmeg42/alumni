from django.urls import path
from . import views

urlpatterns = [
    path("ex-1/alumni", views.alumni_post, name="create"),
]