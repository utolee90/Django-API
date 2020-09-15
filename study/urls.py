from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentView)
router.register('scores', views.ScoreView)
router.register('students/incheon', )

urlpatterns = [
    path('', include(router.urls)),
    # path('students/', views.StudentView),
    # path('students/<id>', views.StudentDetailView),
    # path('scores/', views.ScoreView),
    # path('scores/<id>', views.ScoreDetailView),
    #path('students/', views.StudentView.as_view()),
    #path('students/<pk>', views.StudentDetailView.as_view()),
    #path('scores/', views.ScoreView.as_view()),
    #path('scores/<pk>', views.ScoreDetailView.as_view()),
]
