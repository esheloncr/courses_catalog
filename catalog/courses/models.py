from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,verbose_name="Название курса")
    description = models.TextField(max_length=512, verbose_name="Описание курса")
    course_url = models.URLField(max_length=200, default="#")
    start_date = models.DateField(verbose_name="Дата начала курса")
    end_date = models.DateField(verbose_name="Дата окончания курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title

    """def __repr__(self):
        return self.course_id, self.title, self.description,self.course_url, self.start_date, self.end_date"""
