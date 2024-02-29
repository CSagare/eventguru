from django.urls import path
from . import views

urlpatterns = [
    # path('my-link/', views.my_view, name='my_view'),
    path('',views.index,name='index'),
    path('planners',views.eventplanners,name='planners'),
    # path('contact',views.contact,name='contact'),
    path('contact/', views.contact_view, name='contact'),
    path('about',views.about,name='about'),
    path('defaults/<int:event_id>/', views.defaults, name='defaults')


   

]
