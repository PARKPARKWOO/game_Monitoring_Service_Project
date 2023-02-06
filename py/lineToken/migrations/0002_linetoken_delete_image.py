# Generated by Django 4.1.6 on 2023-02-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lineToken", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LineToken",
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
                ("line_token", models.CharField(max_length=200, unique=True)),
                ("photo_input", models.ImageField(upload_to="")),
                ("want_message", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="Image",
        ),
    ]
