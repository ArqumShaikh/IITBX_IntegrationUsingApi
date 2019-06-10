from django.urls import path
from . import views
urlpatterns = [
    path('grades/', views.grades_view, name='grades'),
]
