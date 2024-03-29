# Generated by Django 4.0.8 on 2023-01-21 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(choices=[(1, 'Trivial'), (2, 'Minor'), (3, 'Major'), (4, 'Critical'), (5, 'Blocker')])),
                ('type', models.IntegerField(choices=[(1, 'Bug'), (2, 'Enhancement'), (3, 'Request'), (4, 'Task')])),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Development'), (3, 'QA'), (4, 'Closed')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
