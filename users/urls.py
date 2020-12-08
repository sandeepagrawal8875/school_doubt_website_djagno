from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', users_views.login_page, name='login'),
    path('logout/', users_views.logout_User, name='logout'),

    path('update/profile/', users_views.profile , name='update_profile'),
    path('profile/', users_views.profileView, name = 'profile'),
]