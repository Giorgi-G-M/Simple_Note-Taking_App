from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
