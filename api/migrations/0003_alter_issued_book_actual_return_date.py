# Generated by Django 4.0.5 on 2022-07-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_issued_book_actual_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issued_book',
            name='actual_return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]