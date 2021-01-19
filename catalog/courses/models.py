from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title, self.description, self.start_date
