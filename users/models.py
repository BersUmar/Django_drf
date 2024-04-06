from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='e-mail')

    avatar = models.ImageField(upload_to='user/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_payment = models.DateField(verbose_name='дата платежа', auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.FloatField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(max_length=50, verbose_name='Способ оплаты', default='in cash')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'