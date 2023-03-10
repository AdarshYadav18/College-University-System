# Generated by Django 4.1.2 on 2023-01-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=50)),
                ('slname', models.CharField(default='not', max_length=30)),
                ('semail', models.EmailField(max_length=254)),
                ('scontact', models.CharField(max_length=50)),
                ('sgender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='something', max_length=128)),
                ('scollege_name', models.CharField(default='not', max_length=40)),
                ('sgrade', models.IntegerField(default='12')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee_model',
        ),
    ]
