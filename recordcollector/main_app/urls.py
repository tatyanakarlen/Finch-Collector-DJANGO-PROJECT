from django.urls import path
from . import views 

urlpatterns = [
    #path('home/', views.home, name='home'), 
    path('', views.home, name='home'), 
    path('about/', views.about), 
    path('records/', views.records_index), 
    path('seed/', views.seed), 
    path('records/<int:record_id>', views.show, name='show')
]


