from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publisher(models.Model):
    class Meta(object):
        db_table = 'publicher'

    name = models.CharField(verbose_name='出版社', max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    class Meta(object):
        db_table = 'author'

    name = models.CharField(verbose_name='著者', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta(object):
        db_table = 'book'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    image = models.ImageField(verbose_name='画像', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author, verbose_name='著者')
    owner = models.ForeignKey(User, verbose_name='所有者', on_delete=models.PROTECT)
    lended = models.BooleanField(verbose_name='貸出中')

    def __str__(self):
        return self.title
