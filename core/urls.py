from django.urls import path
from rest_framework.routers import DefaultRouter

from core.viewsets import TeacherViewSet

urlpatterns = [
    # path('teacher/{pk}/students', TeacherViewSet.as_view({'get': 'list'}), 'teacher'),
    # path('teacher/{pk}/students', require_GET(SampleViewSet.as_view())),
    
    
]

router = DefaultRouter()
router.register('teacher', TeacherViewSet, 'teacher')
urlpatterns += router.urls