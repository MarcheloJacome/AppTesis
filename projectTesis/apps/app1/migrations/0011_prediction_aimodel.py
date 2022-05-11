# Generated by Django 4.0.2 on 2022-05-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_prediction_heartdisease'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='aiModel',
            field=models.CharField(choices=[(0, 'Single Model (K-Nearest Neighbors)'), (1, 'Hard Voting Ensemble Models')], max_length=50, null=True),
        ),
    ]