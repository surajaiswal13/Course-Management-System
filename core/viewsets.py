from rest_framework import viewsets

from core.models import Teacher, Course, Student
from core.serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.prefetch_related().all()
    serializer_class = TeacherSerializer
    http_method_name = ['get']