# Generated by Django 3.2.4 on 2021-07-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_question_questionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='title',
            field=models.TextField(default='title', max_length=255),
        ),
    ]
