from django.urls import path
from . import views

urlpatterns = [
    path('add_fake_data/', views.add_fake_data, name='add_fake_data'),
    path('show_fake_data/', views.show_fake_data, name='show_fake_data'),
]