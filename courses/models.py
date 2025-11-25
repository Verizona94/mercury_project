from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField("Название курса", max_length=200)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена (руб)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField("Тема урока", max_length=200)
    video_url = models.URLField("Ссылка на видео (YouTube/Kinescope)")
    content = models.TextField("Конспект урока", blank=True)
    order = models.PositiveIntegerField("Порядковый номер", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.order}. {self.title}"
