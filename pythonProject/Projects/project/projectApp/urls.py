from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app, name='app'),
    path('index/',views.index,name='index'),
    path('book/',views.book,name='book'),
    path('about/',views.about,name='about'),
]