# Generated by Django 4.1.7 on 2023-03-02 12:57

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=main.utils.user_dir_path),
        ),
    ]