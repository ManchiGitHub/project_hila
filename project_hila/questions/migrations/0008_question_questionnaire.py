# Generated by Django 3.2.4 on 2021-07-17 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_questionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='questions.questionnaire'),
        ),
    ]
