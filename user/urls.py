from django.urls import path    
from . import views

app_name = 'user'


urlpatterns = [
    path('sign-up/', views.register_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('log-out/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'), 
    path('update/', views.update_profile_view, name='update'), 
    path('buy/', views.buy_view, name='buy'),
    path('comingsoon/', views.comingsoon_view, name='comingsoon'),
    path('history', views.history_view, name='history'),
]