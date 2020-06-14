# Generated by Django 2.2.10 on 2020-04-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200403_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='tag_title',
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
    ]
