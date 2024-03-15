# Generated by Django 5.0.3 on 2024-03-13 09:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0005_project_password2_alter_project_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='password',
        ),
        migrations.RemoveField(
            model_name='project',
            name='password2',
        ),
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_At',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='phone',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='zip_code',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='image',
            field=models.FileField(blank=True, upload_to='project_images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]