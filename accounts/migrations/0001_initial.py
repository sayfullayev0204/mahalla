# Generated by Django 5.0.4 on 2024-05-02 11:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mahalla",
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
                ("name", models.CharField(max_length=300)),
                ("overall", models.SmallIntegerField(default=0)),
                ("plan_en_b2", models.SmallIntegerField(default=0)),
                ("plan_en_c1", models.SmallIntegerField(default=0)),
                ("plan_en_c2", models.SmallIntegerField(default=0)),
                ("plan_deorother_b2", models.SmallIntegerField(default=0)),
                ("plan_deorother_c1", models.SmallIntegerField(default=0)),
                ("plan_deorother_c2", models.SmallIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Mahalla",
                "verbose_name_plural": "Mahallalar",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Tuman",
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
                ("name", models.CharField(max_length=300)),
                ("overall", models.SmallIntegerField(default=0)),
                ("plan_en_b2", models.SmallIntegerField(default=0)),
                ("plan_en_c1", models.SmallIntegerField(default=0)),
                ("plan_en_c2", models.SmallIntegerField(default=0)),
                ("plan_deorother_b2", models.SmallIntegerField(default=0)),
                ("plan_deorother_c1", models.SmallIntegerField(default=0)),
                ("plan_deorother_c2", models.SmallIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Tuman",
                "verbose_name_plural": "Tumanlar",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("last_login", models.DateTimeField(auto_now=True)),
                (
                    "role",
                    models.IntegerField(
                        choices=[
                            (7, "Admin"),
                            (6, "Viloyat Hokimi"),
                            (5, "Viloyat Hokimi Yordamchisi"),
                            (4, "Tuman Hokimi"),
                            (3, "Tuman Yoshlar Ishlari Agentligi"),
                            (2, "Mahalla Yoshlar Yshlari Agentligi"),
                            (1, "Maktabdagi mas'ul shaxs"),
                        ],
                        default=2,
                    ),
                ),
                ("rank", models.IntegerField(blank=True, editable=False, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="custom_user_set",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="custom_user_set",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Foydalanuvchi",
                "verbose_name_plural": "Foydalanuvchilar",
                "ordering": ["role", "username"],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Maktab",
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
                ("name", models.CharField(max_length=300)),
                ("overall", models.SmallIntegerField(default=0)),
                ("plan_en_b2", models.SmallIntegerField(default=0)),
                ("plan_en_c1", models.SmallIntegerField(default=0)),
                ("plan_en_c2", models.SmallIntegerField(default=0)),
                ("plan_deorother_b2", models.SmallIntegerField(default=0)),
                ("plan_deorother_c1", models.SmallIntegerField(default=0)),
                ("plan_deorother_c2", models.SmallIntegerField(default=0)),
                (
                    "mahalla",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.mahalla",
                    ),
                ),
            ],
            options={
                "verbose_name": "Maktab",
                "verbose_name_plural": "Maktablar",
                "ordering": ["name"],
            },
        ),
        migrations.AddConstraint(
            model_name="tuman",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("plan_en_b2__lte", models.F("overall")),
                    ("plan_en_c1__lte", models.F("overall")),
                    ("plan_en_c2__lte", models.F("overall")),
                    ("plan_deorother_b2__lte", models.F("overall")),
                    ("plan_deorother_c1__lte", models.F("overall")),
                    ("plan_deorother_c2__lte", models.F("overall")),
                ),
                name="tuman_plan_constraint",
            ),
        ),
        migrations.AddField(
            model_name="maktab",
            name="tuman",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.tuman",
            ),
        ),
        migrations.AddField(
            model_name="mahalla",
            name="tuman",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.tuman"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tuman",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.tuman",
            ),
        ),
        migrations.AddConstraint(
            model_name="maktab",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("plan_en_b2__lte", models.F("overall")),
                    ("plan_en_c1__lte", models.F("overall")),
                    ("plan_en_c2__lte", models.F("overall")),
                    ("plan_deorother_b2__lte", models.F("overall")),
                    ("plan_deorother_c1__lte", models.F("overall")),
                    ("plan_deorother_c2__lte", models.F("overall")),
                ),
                name="maktab_plan_constraint",
            ),
        ),
        migrations.AddConstraint(
            model_name="mahalla",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("plan_en_b2__lte", models.F("overall")),
                    ("plan_en_c1__lte", models.F("overall")),
                    ("plan_en_c2__lte", models.F("overall")),
                    ("plan_deorother_b2__lte", models.F("overall")),
                    ("plan_deorother_c1__lte", models.F("overall")),
                    ("plan_deorother_c2__lte", models.F("overall")),
                ),
                name="mahalla_plan_constraint",
            ),
        ),
    ]