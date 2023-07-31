# coding=utf-8

from django.db import models
from datetime import datetime


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author

    def get_previous_book(self):
        """
        Получает предыдущую книгу по дате
        """
        return Book.objects.filter(pub_date__lt=self.pub_date).order_by('-pub_date').first()

    def get_next_book(self):
        """
        Получает следующую книгу по дате
        """
        return Book.objects.filter(pub_date__gt=self.pub_date).order_by('pub_date').first()

    def get_pub_date_path(self):
        """
        Преобразует дату книги в формат url запроса
        """
        old_date = self.pub_date
        return old_date.strftime('%Y-%m-%d')