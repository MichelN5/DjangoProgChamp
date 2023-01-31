# Generated by Django 3.2.2 on 2022-08-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenges', '0004_alter_challenge_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='default_code',
            field=models.TextField(default='hello', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='testcases_code',
            field=models.TextField(default='hello', max_length=500),
            preserve_default=False,
        ),
    ]
