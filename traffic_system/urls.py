from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/intersection-state/', views.get_intersection_state, name='get-state'),
    
    
    path('api/set-intersection-plan/', views.set_intersection_plan, name='set-plan'),
    
    path('admin/', admin.site.urls),
]