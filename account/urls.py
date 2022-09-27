from django.urls import path
from . import views
app_name = 'account'




urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('like/',views.like,name='like')

]


