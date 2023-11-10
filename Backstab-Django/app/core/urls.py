from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('pricing', views.get_price, name='pricing'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)