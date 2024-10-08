from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like'),
    path('share/<int:phpto_id>/', views.share_functionality, name='share'),
]
