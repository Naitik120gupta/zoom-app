from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView,LoginView
from . import views


urlpatterns = [
   path('signup/', RegisterView.as_view(), name='signup'),
   path('login/', LoginView.as_view(), name='login'),
   path('info/',views.userInfo), 
]
