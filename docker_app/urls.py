from django.urls import path
from .views import home, about, gallery

urlpatterns = [
    path('', home, name='home'), 
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
]
