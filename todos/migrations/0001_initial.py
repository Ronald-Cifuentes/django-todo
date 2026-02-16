# Generated migration for todos app (schema matches Prisma/Node)

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.CharField(editable=False, max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'todos',
                'ordering': ['-created_at'],
            },
        ),
    ]
