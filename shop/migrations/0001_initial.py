# Generated by Django 2.1.5 on 2019-02-06 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='著者')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像')),
                ('lended', models.BooleanField(verbose_name='貸出中')),
                ('authors', models.ManyToManyField(to='shop.Author', verbose_name='著者')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='所有者')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='出版社')),
            ],
            options={
                'db_table': 'publicher',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.Publisher', verbose_name='出版社'),
        ),
    ]
