# Generated by Django 4.0.6 on 2022-07-20 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_tag_alter_publication_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['-id', 'name']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-id', 'name']},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='tags',
        ),
    ]
