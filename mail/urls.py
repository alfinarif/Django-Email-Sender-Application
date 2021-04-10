from django.urls import path
from .views import EmailSanderView


urlpatterns = [
    path('', EmailSanderView.as_view(), name='index'),
]