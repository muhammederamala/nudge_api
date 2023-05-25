# Generated by Django 4.1.2 on 2023-05-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="nudge_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="nudge_images/"),
                ),
                ("tagline", models.CharField(max_length=100)),
                ("schedule", models.DateTimeField()),
                ("description", models.TextField()),
                ("moderator", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("sub_category", models.CharField(max_length=100)),
                ("rigor_rank", models.IntegerField()),
            ],
        ),
    ]