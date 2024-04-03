from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(verbose_name='Превью', upload_to='course/')

    def __str__(self):
        return f'{self.name} {self.desc}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(verbose_name='Превью', upload_to='course/')
    video_link = models.URLField(verbose_name='Ссылка', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.desc}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'