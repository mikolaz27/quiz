# Generated by Django 3.2.13 on 2022-04-27 20:05

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ("title", models.CharField(max_length=64)),
                ("description", models.TextField(blank=True, max_length=1024, null=True)),
                (
                    "level",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Basic"), (1, "Middle"), (2, "Advanced")], default=1
                    ),
                ),
                ("image", models.ImageField(default="default.png", upload_to="media/covers")),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "order_number",
                    models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
                ),
                ("text", models.CharField(max_length=64)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="questions", to="quiz.quiz"
                    ),
                ),
            ],
        ),
    ]
