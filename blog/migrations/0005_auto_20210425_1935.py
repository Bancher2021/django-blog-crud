# Generated by Django 3.1.7 on 2021-04-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
