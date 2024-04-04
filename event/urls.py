from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('my-link/', views.my_view, name='my_view'),
    path('',views.index,name='index'),
    path('planners',views.eventplanners,name='planners'),
    # path('contact',views.contact,name='contact'),
    path('contact/', views.contact_view, name='contact'),
    path('about',views.about,name='about'),
    path('defaults/<int:event_id>/', views.defaults, name='defaults'),
    path('planner/search/', views.search, name='planner_search'),
    path('show', views.home, name='show'),
    path('recommendations', views.recommendations, name='recommendations'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)