# Generated by Django 5.1.6 on 2025-02-13 16:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0002_alter_author_birth_date_alter_author_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('site', models.URLField(blank=True, null=True, verbose_name='Site')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('Gender', models.CharField(max_length=50, verbose_name='Gender')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(120)], verbose_name='Age')),
                ('role', models.CharField(choices=[('member', 'Member'), ('admin', 'Admin'), ('employee', 'Employee')], max_length=50, verbose_name='Role')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('library', models.ManyToManyField(related_name='members', to='lib_app.library', verbose_name='Library')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('genre', models.CharField(choices=[('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction'), ('science fiction', 'Science Fiction'), ('fantasy', 'Fantasy'), ('mystery', 'Mystery'), ('biography', 'Biography')], default='N/A', max_length=100, verbose_name='Genre')),
                ('page_count', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Page count')),
                ('pub_date', models.DateField(blank=True, null=True, verbose_name='Pub date')),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lib_app.author')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='lib_app.category', verbose_name='Category ID')),
                ('library_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='lib_app.library')),
                ('member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lib_app.member')),
            ],
        ),
    ]
