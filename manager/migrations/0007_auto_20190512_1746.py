# Generated by Django 2.2.1 on 2019-05-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_expertstotopics'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionrating',
            name='expert_rating',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solutionrating',
            name='rating',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]