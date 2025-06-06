from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('url', models.URLField()),
            ],
        ),
    ]
