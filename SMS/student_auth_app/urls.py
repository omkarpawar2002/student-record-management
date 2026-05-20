from django.urls import path
from .views import ( sign_up , sign_in , sign_out )

urlpatterns = [
    path('sign_up/',sign_up,name='Sign_Up'),
    path('sign_in/',sign_in,name='Sign_In'),
    path('sign_out/',sign_out,name='Sign_Out')
]