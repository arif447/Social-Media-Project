from django.urls import path
from App_Post import views
app_name = 'App_Post'

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('post/', views.user_post, name='post'),
    path('like/<pk>/', views.Like_user, name='like'),
    path('unlike/<pk>/', views.Unlike_user, name='unlike'),

]
