# Generated by Django 3.1.5 on 2021-04-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='modelPath',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='expectedReply',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
