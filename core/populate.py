from core.models import Teacher, Course, Student

s1 = Student.objects.create(name="StudA")
s1.save()
s2 = Student.objects.create(name="StudB")
s2.save()
s3 = Student.objects.create(name="StudC")
s3.save()