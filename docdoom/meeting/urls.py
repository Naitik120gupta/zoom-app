from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView,LoginView
from . import views


urlpatterns = [
   path('signup/', RegisterView.as_view(), name='signup'),
   path('login/', LoginView.as_view(), name='login'),
   path('info/',views.userInfo), 

   path(' ', views.index, name='agora-index'),
   path('pusher/auth/', views.pusher_auth, name='agora-pusher-auth'),
   path('token/', views.generate_agora_token, name='agora-token'),
   path('call-user/', views.call_user, name='agora-call-user'),
]
