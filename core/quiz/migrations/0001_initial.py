# Generated by Django 4.2.10 on 2024-02-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(null=True)),
                ('op1', models.CharField(max_length=255, null=True)),
                ('op2', models.CharField(max_length=255, null=True)),
                ('op3', models.CharField(max_length=255, null=True)),
                ('op4', models.CharField(max_length=255, null=True)),
                ('ans', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]