# Generated by Django 2.2.14 on 2020-08-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_personal_statement_ps_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UoB_Year_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UoB_Year_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UoB_Year_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=200)),
            ],
        ),
    ]