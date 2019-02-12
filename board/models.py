from django.db import models
from django.contrib.auth.models import User
from shop.models import Book

# Create your models here.
class Summary(models.Model):
    class Meta(object):
        db_table = 'summary'

    book = models.ForeignKey(Book, verbose_name='書籍', on_delete=models.PROTECT)
    writer = models.ForeignKey(User, verbose_name='執筆者', on_delete=models.PROTECT)
    summary_title = models.CharField(verbose_name='タイトル', max_length=255)
    summary_text = models.TextField(verbose_name='本文', max_length=100)

    def __str__(self):
        return self.summary_title
