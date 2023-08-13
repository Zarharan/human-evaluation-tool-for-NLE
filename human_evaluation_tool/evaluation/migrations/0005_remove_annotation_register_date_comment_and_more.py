# Generated by Django 4.2.4 on 2023-08-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_rename_generated_explanation_instance_explanation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='register_date_comment',
        ),
        migrations.AlterField(
            model_name='annotation',
            name='claim_repetition',
            field=models.BooleanField(help_text=' Is the claim text repeated in the generated explanation?', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='claim_repetition_comment',
            field=models.TextField(help_text='Any comment on your choice of claim repetition'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='external_consistency',
            field=models.IntegerField(choices=[(1, 'Highly inconsistent (full of inconsistencies)'), (2, 'Mostly inconsistent'), (3, 'Some inconsistencies'), (4, 'Mostly consistent'), (5, 'Highly consistent (no inconsistencies)')], help_text='Is the generated explanation externally consistent, i.e. consistent with the context?', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='external_consistency_comment',
            field=models.TextField(help_text='Any comment on your choice of external consistency'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='extra_information',
            field=models.BooleanField(help_text='Does the generated explanation contain extra information that is not mentioned in the claim or in the context?', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='extra_information_comment',
            field=models.TextField(help_text='Any comment on your choice of extra information'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='fluency',
            field=models.IntegerField(choices=[(1, 'Incomprehensible'), (2, 'Disfluent English'), (3, 'None-native English'), (4, 'Good English'), (5, 'Flawless English')], help_text='The fluency of the generated explanation.', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='fluency_comment',
            field=models.TextField(help_text='Any comment on your choice of fluency'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='internal_consistency',
            field=models.IntegerField(choices=[(1, 'Highly inconsistent (full of inconsistencies)'), (2, 'Mostly inconsistent'), (3, 'Some inconsistencies'), (4, 'Mostly consistent'), (5, 'Highly consistent (no inconsistencies)')], help_text='Is the generated explanation internally consistent?', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='internal_consistency_comment',
            field=models.TextField(help_text='Any comment on your choice of internal consistency'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='internal_repetition',
            field=models.BooleanField(help_text='Does the generated explanation contain repeated information?', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='internal_repetition_comment',
            field=models.TextField(help_text='Any comment on your choice of internal repetition'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='missing_information',
            field=models.IntegerField(choices=[(0, 'Crucial information is missing'), (1, 'Some minor detail is missing'), (2, 'The explanation contains all the information needed')], help_text='Is the generated explanation missing information from the context that is important in explaining the veracity of the claim?', null=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='missing_information_comment',
            field=models.TextField(help_text='Any comment on your choice of missing information'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='suggested_class',
            field=models.IntegerField(choices=[(0, 'False'), (1, 'True'), (2, 'Mixture'), (3, 'Unproven')], help_text='Choose the factuality of the claim by considering the generated explanation.', null=True, verbose_name='Suggested Class'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='suggested_class_comment',
            field=models.TextField(help_text='Any comment on your choice of suggested class'),
        ),
    ]
