# Generated by Django 3.0 on 2020-04-30 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handouts', '0001_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='year_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Year_Level'),
        ),
        migrations.AddField(
            model_name='handouts',
            name='year_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Year_Level'),
        ),
    ]
