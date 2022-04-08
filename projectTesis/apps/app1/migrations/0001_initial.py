# Generated by Django 4.0.2 on 2022-02-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('sex', models.BooleanField()),
                ('chestPainType', models.IntegerField(choices=[(0, 'Asymptomatic'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Typical Angina')])),
                ('restingBP', models.PositiveIntegerField()),
                ('cholesterol', models.PositiveIntegerField()),
                ('fastingBS', models.BooleanField()),
                ('restingECG', models.IntegerField(choices=[(0, 'LVH'), (1, 'Normal'), (2, 'ST')])),
                ('maxHR', models.PositiveIntegerField()),
                ('exerciseAngina', models.BooleanField()),
                ('oldpeak', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sT_Slope', models.IntegerField(choices=[(0, 'DOWN'), (1, 'FLAT'), (2, 'UP')])),
                ('heartDisease', models.BooleanField()),
            ],
        ),
    ]
