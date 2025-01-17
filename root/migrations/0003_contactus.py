# Generated by Django 5.1.1 on 2024-12-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_score_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]