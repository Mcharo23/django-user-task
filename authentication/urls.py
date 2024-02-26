from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, UserViewSet

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('',
    #      UserViewSet.as_view({'post': 'auth'}), name='auth-view'),
    # path(
    #     'register/', UserViewSet.as_view({'post': 'register'}), name='register'),
]
