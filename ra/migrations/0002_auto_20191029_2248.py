# Generated by Django 2.2.6 on 2019-10-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ra', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objeto',
            old_name='path_modelo',
            new_name='path_modelo_OBJ',
        ),
        migrations.AddField(
            model_name='objeto',
            name='path_modelo_MTL',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
