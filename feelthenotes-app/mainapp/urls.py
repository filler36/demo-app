from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('status', views.status, name='status'),
    path('notes', views.notes, name='notes'),
    path('notes/<int:note_id>', views.note, name='note')
]