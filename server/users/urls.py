from django.urls import path
from .views import CurrentUserRetrieve, UserAuth, UserCreate, UserLogout, UserRetrieve, UserList

urlpatterns = [
    path('signup', UserCreate.as_view(), name='user_create'),
    path('<int:pk>', UserRetrieve.as_view(), name='user_retrieve'),
    path('auth', UserAuth.as_view(), name='user_auth'),
    path('me', CurrentUserRetrieve.as_view(), name='current_user'),
    path('logout', UserLogout.as_view(), name='user_logout'),
    path('', UserList.as_view(), name='user_list')

]
