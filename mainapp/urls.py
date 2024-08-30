from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('food/<slug:slug>/', FoodDetailView.as_view(), name='food_slug'),
    path('reg/', RegView.as_view(), name='reg')
]
