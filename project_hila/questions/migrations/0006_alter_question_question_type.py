# Generated by Django 3.2.4 on 2021-06-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_alter_question_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('בחירה יחידה', 'בחירה יחידה'), ('בחירה מרובה', 'בחירה מרובה'), ('שאלה פתוחה', 'שאלה פתוחה')], default='OpenQuestion', max_length=20),
        ),
    ]
