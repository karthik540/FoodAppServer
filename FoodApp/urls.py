from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('phoneAuth/', views.phoneAuthentication , name = 'phoneAuth'),
    path('phoneVerify/', views.checkVerificationCode , name = 'phoneVerify')
]