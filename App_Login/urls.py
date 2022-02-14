from django.urls import path
from App_Login import views
app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.Sign_up, name='Sign_up'),
    path('login/', views.Login_user, name='Login_user'),
    path('logout', views.Logout_user, name='Logout_user'),
    path('edit/', views.Edit_Profile, name='Edit_Profile'),
    path('profile/', views.user_profile, name='user_profile'),
    path('user_other/<username>/', views.User_other, name='user_other'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.Unfollow, name='unfollow'),

]



