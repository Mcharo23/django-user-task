from django.urls import path
from .views import getRoutes, RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('auth/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user-view'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
