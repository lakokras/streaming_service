from django.urls import path
import myapp.views as myapp

app_name = 'myapp'

urlpatterns = [
    path('', myapp.accommodations, name='index'),
    path('accommodation_details/<int:pk>/', myapp.accommodation,
         name='accommodation'),
]
