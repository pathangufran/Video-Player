# Generated by Django 4.1.10 on 2023-08-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0009_name_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
