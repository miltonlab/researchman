from django.db import models

# Create your models here.

class Career(models.Model):
    name = models.CharField(max_length=80) 
    faculty = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class AcademicTitle(models.Model):
    LEVELS = (
        ('3', 'Tercer Nivel'),
        ('4E', 'Especialidad'),
        ('4M', 'Maestría'),
        ('4D', 'Doctorado'),
    )
    level = models.CharField(max_length=2, choices=LEVELS)
    name = models.CharField(max_length=100)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    work_email = models.EmailField()
    personal_email = models.EmailField()
    titles = models.ManyToManyField(AcademicTitle)
    career = models.ForeignKey(Career)

    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Researcher(models.Model):
    teacher = models.OneToOneField(Teacher, primary_key=True)

    def __str__(self):
        return self.teacher
    


