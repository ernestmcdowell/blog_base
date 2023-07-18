# Generated by Django 4.2.3 on 2023-07-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='technology',
            field=models.ManyToManyField(to='blog.techstack'),
        ),
    ]
