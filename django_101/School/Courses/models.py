from django.db import models

class Course_info(models.Model):
    course_name = models.CharField(max_length=50)
    course_number = models.IntegerField(help_text = "Course Number represents the Course ID")
