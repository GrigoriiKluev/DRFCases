# Generated by Django 4.1.6 on 2023-02-07 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0005_alter_post_views_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['post']},
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('post', 'comment_text')},
        ),
    ]