# Generated by Django 2.1.4 on 2019-10-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('comment', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='photos')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
