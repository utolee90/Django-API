from django.urls import path, include
from . import views
urlpatterns = [
    path('students/', views.StudentView),
    path('students/<id>', views.StudentDetailView),
    path('scores/', views.ScoreView),
    path('scores/<id>', views.ScoreDetailView)
]