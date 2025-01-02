# Generated by Django 4.2.17 on 2025-01-02 06:43

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
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('time', models.IntegerField(default=0)),
                ('video', models.FileField(upload_to='film/%Y/%m/%d')),
                ('image', models.ImageField(upload_to='film/%Y/%m/%d')),
                ('translate_time', models.DateTimeField(auto_now_add=True)),
                ('views_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('dis_like_count', models.IntegerField(default=0)),
                ('like', models.BooleanField(default=False)),
                ('dis_like', models.BooleanField(default=False)),
                ('actor', models.ManyToManyField(related_name='films', to='film.actor')),
                ('director', models.ManyToManyField(related_name='films', to='film.director')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='film.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(related_name='films', to='film.genre'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('like_count', models.IntegerField(default=0)),
                ('dis_like_count', models.IntegerField(default=0)),
                ('like', models.BooleanField(default=False)),
                ('dis_like', models.BooleanField(default=False)),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='film.film')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
