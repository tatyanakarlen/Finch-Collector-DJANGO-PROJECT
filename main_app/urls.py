from django.urls import path
from . import views 

urlpatterns = [
    #path('home/', views.home, name='home'), 
    path('', views.home, name='home'), 
    path('about/', views.about), 
    path('records/', views.records_index), 
    path('records/<int:record_id>', views.records_detail, name='detail'), 
    #shows user the form to create record 
    path('records/new_record/', views.RecordCreate.as_view(), name='record_create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='record_update'), 
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='record_delete'), 
]





