from django.urls import path
app_name = 'blog'
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search')
]