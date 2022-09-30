from django.urls import path 
app_name = 'contact'
from . import views
urlpatterns = [
   path('reach_out_to_us/',views.ContactView.as_view(),name='contact'),
   path('success/',views.ContactSuccessView.as_view(),name='success'),
]
