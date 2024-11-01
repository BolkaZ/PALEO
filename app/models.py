from django.db import models
from django.contrib.auth.models import User

class Period(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название периода")
    detail_text = models.TextField(verbose_name="Описание периода")
    start = models.CharField(max_length=50, verbose_name="Начало периода")
    end = models.CharField(max_length=50, verbose_name="Окончание периода")
    found_quantity = models.PositiveIntegerField(verbose_name="Количество найденных окаменелостей")
    image = models.URLField(max_length=500, verbose_name="Изображение периода")
    
    def __str__(self):
        return self.name

class Animal(models.Model):
    period = models.ForeignKey(Period, related_name='animals', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    quantity_found = models.IntegerField()

    def __str__(self):
        return self.name

class Bid(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # Разрешить null
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        return f"Bid for {self.period.name} by {self.user.username if self.user else 'No User'}"
