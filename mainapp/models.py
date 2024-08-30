from django.db import models
from django.urls import reverse, reverse_lazy
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class FoodModel(models.Model):
    name = models.CharField('Названия: ', max_length=60)
    about = models.TextField('Описание:')
    pic = models.ImageField('Картинка:', upload_to='food/')
    upload_date = models.DateTimeField('Дата загрузки:', auto_now_add=True)
    updated_date = models.DateTimeField('Дата изминения:', auto_now=True)
    is_exclusive = models.BooleanField(default=False)
    price = models.DecimalField('Цена: ', validators=[MinValueValidator(0.0)], decimal_places=2, max_digits=6)
    slug = models.SlugField('Slug')
    category = models.ForeignKey("Category", verbose_name="Категория:", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_slug', kwargs={'slug': self.slug})


class Category(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category


class WorkersModels(models.Model):
    fname = models.CharField('name', max_length=50)
    work = models.CharField('work', max_length=50)
    img = models.ImageField('Картинка:', upload_to='workers/')
    instagram = models.URLField('instagram', blank=True)
    facebook = models.URLField('facebook', blank=True)
    twitter = models.URLField('twitte', blank=True)

    class Meta:
        verbose_name = "Повар"
        verbose_name_plural = "Повара"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('chef_detail', kwargs={'pk': self.pk})



class Booking(models.Model):

    boking_time=[
        ('09:00', '09:00AM'),
        ('10:00', '10:00AM'),
        ('11:00', '11:00AM'),
        ('13:00', '01:00PM'),
        ('14:00', '02:00PM'),
        ('15:00', '03:00PM'),
        ('16:00', '04:00PM'),
        ('17:00', '05:00PM'),
        ('18:00', '06:00PM'),
        ('19:00', '07:00PM'),
        ('20:00', '08:00PM'),
        ('21:00', '09:00PM'),
        ('22:00', '10:00PM'),

    ]
    fname = models.CharField("имя", max_length=50)
    gmail = models.EmailField('вам gmail', max_length=50)
    persons = models.PositiveIntegerField("количество персон", validators= [MaxValueValidator(100), MinValueValidator(1)])
    numbers = models.CharField('ваш номер' , max_length=14)
    message = models.TextField('ваше сообщение', max_length=300)
    date = models.DateField('дата')
    time = models.CharField('время брони', blank=True, max_length=30, choices=boking_time, default=boking_time[0])

    class Meta:
        verbose_name ="Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse_lazy('main')

class Feedback(models.Model):
    fname = models.CharField('имя', max_length=50)
    work = models.CharField('работает в', max_length=100)
    text = models.TextField('сообщение')
    img = models.ImageField('Картинка:', upload_to='workers/')

    class Meta:
        verbose_name ="Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.fname