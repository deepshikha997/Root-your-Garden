from django.urls import path
from . import views

urlpatterns = [
path('',views.register,name='reg'),
path('gardenreg',views.gardenreg,name='gardenreg'),
path('login',views.login,name='garlgt'),
path('login',views.login,name='lgt'),
path('recover',views.recoverpwd,name='recover'),
path('password_reset_complete',views.Pwdcomplete,name='password_reset_complete'),
path('logout',views.logout,name='lgn'),
path('profile',views.Prof,name='pro'),
path('uppro',views.uppro,name='uppro'),
]