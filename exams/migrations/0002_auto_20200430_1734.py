# Generated by Django 3.0 on 2020-04-30 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '0001_initial'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams_answers', to='quiz.Student'),
        ),
        migrations.AddField(
            model_name='question',
            name='exams',
            field=models.ForeignKey(help_text='Exams', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Exams'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(help_text='Question', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exams.Question'),
        ),
    ]