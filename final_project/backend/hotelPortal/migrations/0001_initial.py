# Generated by Django 4.1.1 on 2022-11-25 18:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("age", models.PositiveIntegerField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, max_length=10, null=True)),
                ("tele", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
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
                (
                    "price",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Unpaid", "Unpaid"),
                            ("Paid", "Paid"),
                            ("Canceled", "Canceled"),
                        ],
                        default="Unpaid",
                        max_length=8,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Standard", "Standard"),
                            ("Deluxe", "Deluxe"),
                            ("Connecting", "Connecting"),
                            ("Suite", "Suite"),
                        ],
                        default="Standard",
                        max_length=10,
                    ),
                ),
                (
                    "occupancy",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                ("roomNum", models.CharField(max_length=5)),
                (
                    "direction",
                    models.CharField(
                        choices=[
                            ("North", "North"),
                            ("South", "South"),
                            ("East", "East"),
                            ("West", "West"),
                        ],
                        default="North",
                        max_length=12,
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("roomPicture", models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("startTime", models.DateField(blank=True, null=True)),
                ("endTime", models.DateField(blank=True, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="hotelPortal.client",
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="hotelPortal.payment",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="hotelPortal.room",
                    ),
                ),
            ],
        ),
    ]
