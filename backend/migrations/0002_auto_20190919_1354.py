# Generated by Django 2.1.2 on 2019-09-19 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookchacter',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='bookchacterimage',
            old_name='book_id',
            new_name='book',
        ),
    ]
