# Generated by Django 5.1.6 on 2025-02-13 16:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0003_category_library_member_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='deleted',
            field=models.BooleanField(default=False, help_text='False - active author, True - inactive', verbose_name='Profile link'),
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField()),
                ('birth_city', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='lib_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(blank=True, null=True, verbose_name='Borrow date')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='Return date')),
                ('returned', models.BooleanField(default=False, verbose_name='Returned')),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='lib_app.author')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='lib_app.book')),
                ('library', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='lib_app.library')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('books', models.ManyToManyField(related_name='events', to='lib_app.book')),
                ('library', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='lib_app.library')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(blank=True, null=True, verbose_name='Registration date')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='lib_app.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='lib_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique_for_date='create_date', verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('moderated', models.BooleanField(default=False, verbose_name='Moderated')),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(auto_now=True)),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='lib_app.author')),
                ('library', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='lib_app.library')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='lib_app.book')),
                ('reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='lib_app.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='review_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lib_app.review', verbose_name='Review'),
        ),
    ]
