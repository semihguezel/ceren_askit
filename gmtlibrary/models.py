from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % self.name


class Academician(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class LectureNotes(models.Model):
    name = models.CharField(max_length=30)
    academician = models.ForeignKey(Academician, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class StudentNotes(models.Model):
    name = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
