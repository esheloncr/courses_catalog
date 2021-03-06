from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,verbose_name="Название курса")
    description = models.TextField(max_length=512, verbose_name="Описание курса")
    start_date = models.DateField(verbose_name="Дата начала курса")
    end_date = models.DateField(verbose_name="Дата окончания курса")
    author = models.ForeignKey(User,verbose_name="Автор поста",on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title
