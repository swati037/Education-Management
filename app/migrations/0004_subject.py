# Generated by Django 3.1.7 on 2021-08-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210828_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=100)),
                ('subjectname', models.CharField(max_length=30)),
                ('marks', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
