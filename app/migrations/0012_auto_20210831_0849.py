# Generated by Django 3.1.7 on 2021-08-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210831_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ass',
            name='date',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='ass',
            name='question',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AlterField(
            model_name='ass',
            name='subjectname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='ass',
            name='time',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='testtable',
            name='subjectname3',
            field=models.CharField(default='', max_length=30),
        ),
    ]