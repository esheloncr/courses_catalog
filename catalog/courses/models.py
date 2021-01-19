from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    course_url = models.URLField(max_length=200, default="#")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.course_id, self.title, self.description,self.course_url, self.start_date, self.end_date
