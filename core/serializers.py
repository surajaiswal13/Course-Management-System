from rest_framework import serializers

from core.models import Teacher, Course, Student

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']

class TeacherSerializer(serializers.ModelSerializer):
    student_name = TestSerializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['teacher', 'student', 'student_name']