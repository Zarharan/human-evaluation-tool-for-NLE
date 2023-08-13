# Generated by Django 4.2.4 on 2023-08-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_annotation_annotated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='external_consistency',
            field=models.IntegerField(choices=[(1, 'Highly inconsistent (full of inconsistencies)'), (2, 'Mostly inconsistent'), (3, 'Some inconsistencies'), (4, 'Mostly consistent'), (5, 'Highly consistent (no inconsistencies)')], null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='fluency',
            field=models.IntegerField(choices=[(1, 'Incomprehensible'), (2, 'Disfluent English'), (3, 'None-native English'), (4, 'Good English'), (5, 'Flawless English')], null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='internal_consistency',
            field=models.IntegerField(choices=[(1, 'Highly inconsistent (full of inconsistencies)'), (2, 'Mostly inconsistent'), (3, 'Some inconsistencies'), (4, 'Mostly consistent'), (5, 'Highly consistent (no inconsistencies)')], null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='missing_information',
            field=models.IntegerField(choices=[(0, 'Crucial information is missing'), (1, 'Some minor detail is missing'), (2, 'The explanation contains all the information needed')], null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='suggested_class',
            field=models.IntegerField(choices=[(0, 'False'), (1, 'True'), (2, 'Mixture'), (3, 'Unproven')], null=True),
        ),
    ]