from django.urls import path
#from .views import home_page
from . import views


urlpatterns = [
    path("users/", views.user_list, name="user-list"),
]