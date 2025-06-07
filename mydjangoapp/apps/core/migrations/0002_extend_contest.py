from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='job_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='education_level',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='salary',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
