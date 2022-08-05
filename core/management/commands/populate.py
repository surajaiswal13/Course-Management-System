from django.core.management.base import BaseCommand
# from django.utils import timezone
from core.models import Teacher, Course, Student

class Command(BaseCommand):
    help = '##$'

    def handle(self, *args, **kwargs):
        # time = timezone.now().strftime('%X')
        # s1 = Student.objects.create(name="StudA")
        # s1.save()
        # s2 = Student.objects.create(name="StudB")
        # s2.save()
        # s3 = Student.objects.create(name="StudC")
        # s3.save()
        # t1 = Teacher.objects.create(name="TeachA") 
        # t1.save()
        # t2 = Teacher.objects.create(name="TeachB")
        # t2.save()
        # t3 = Teacher.objects.create(name="TeachC")
        # t3.save()
        # t1 = Teacher.objects.get(name="TeachA") 
        # t2 = Teacher.objects.get(name="TeachB")
        # t3 = Teacher.objects.get(name="TeachC")

        # c1 = Course.objects.create(name="Course1", teacher=t1)
        # c1.save()
        # c2 = Course.objects.create(name="Course2", teacher=t2)
        # c2.save()
        # c3 = Course.objects.create(name="Course3", teacher=t3)
        # c3.save()

        s1 = Student.objects.get(name="StudA")
        s2 = Student.objects.get(name="StudB")
        s3 = Student.objects.get(name="StudC")

        c1 = Course.objects.get(name="Course1")
        c2 = Course.objects.get(name="Course2")
        c3 = Course.objects.get(name="Course3")
        c1.student.add(s1, s2)
        c2.student.add(s1, s3)
        c3.student.add(s2, s3)
        c1.save()
        c2.save()
        c3.save()

        self.stdout.write("Coyrses Saved")