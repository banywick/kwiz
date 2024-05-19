from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone





EventType_Choices = (
    ("Интеллектуальный квиз", "Интеллектуальный квиз"),
    ("Музыкальный квиз", "Музыкальный квиз"),
    ("Спортивное мероприятие", "Спортивное мероприятие"),
    ("Классическая Мафия", "Классическая Мафия"),
    ("Своя Игра", "Своя Игра"),
    ("Интеллектуальная игра 100к1", "Интеллектуальная игра 100к1"),
    ("Брейн-ринг", "Брейн-ринг")
)

EducationLevel_Choices = (
    ("Младшее звено 1-4 классы", "Младшее звено 1-4 класс"),
    ("Среднее звено 5-7 классы", "Среднее звено 5-7 классы"),
    ("Старшее звено 8-11 классы", "Старшее звено 8-11 классы")
)

klass_Choices = (
    ('5А','5А'),
    ('5Б','5Б'),
    ('5В','5В'),
    ('5Г','5Г'),
    ('6А','6А'),
    ('6Б','6Б'),
    ('6В','6В'),
    ('6Г','6Г'),
    ('7А','7А'),
    ('7Б','7Б'),
    ('7В','7В'),
    ('7Г','7Г'),
    ('8А','8А'),
    ('8Б','8Б'),
    ('8В','8В'),
    ('8Г','8Г'),
    ('9А','9А'),
    ('9Б','9Б'),
    ('9В','9В'),
    ('9Г','9Г'),
    ('10А','10А'),
    ('10Б','10Б'),
    ('10В','10В'),
    ('10Г','10Г'),
    ('11А','11А'),
    ('11Б','11Б'),
    ('11В','11В'),
    ('11Г','11Г'),
)

Status_Choices = (
    ("На рассмотрении", "На рассмотрении"),
    ("Принята", "Принята"),
    ("Отклонена", "Отклонена"),
    ("Отменена", "Отменена"),
    ("Посещено", "Посещено")
)


class CustomUser(AbstractUser):
    class_scool = models.CharField(max_length=10, choices=klass_Choices)


class EventType(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование типа мероприятия',
                            choices=EventType_Choices)

    def __str__(self):
        return f"{self.name}"


class EducationLevel(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Наименование степени обучающихся (звена)',
                            choices=EducationLevel_Choices)

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    max_eventers = models.IntegerField(default=100)
    location = models.CharField(max_length=255, null=True, blank=True)
    date_event = models.DateTimeField(null=True, blank=True)
    event_type = models.ForeignKey('EventType', on_delete=models.CASCADE)
    education_level = models.ForeignKey('EducationLevel', on_delete=models.CASCADE)
    responsible = models.ForeignKey('CustomUser', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("detail_event", kwargs={"pk": self.pk})
    
    

class Application(models.Model):
    date_submitted = models.DateField(blank=True, null=True)
    event = models.ForeignKey('Event', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user}, {self.date_submitted}"


class Results(models.Model):
    event = models.ForeignKey('Event', null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.description)


class Post(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    user = models.ForeignKey('CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    time_submit = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return f"{self.title} | {self.user}"

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.pk)))


class Feedback(models.Model):
    feedback = models.TextField(null=True, blank=True)
    time_submit = models.DateTimeField(null=True, blank=True, default=timezone.now)
    user = models.ForeignKey('CustomUser', blank=True, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', blank=True, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.feedback)

class Status(models.Model):
    title = models.CharField(max_length=255, verbose_name='Статус заявки', choices=Status_Choices, blank=True)

    def __str__(self):
        return str(self.title)