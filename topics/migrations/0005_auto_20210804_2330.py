# Generated by Django 3.1.4 on 2021-08-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_projecttopics_topic_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttopics',
            name='topic_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
