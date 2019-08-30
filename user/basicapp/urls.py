from django.urls import  path,include
from basicapp import views

app_name= 'basicapp'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='user_logout'),
    path('login/',views.user_login,name= 'user_login'),
]