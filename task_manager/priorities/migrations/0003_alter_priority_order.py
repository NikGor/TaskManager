# Generated by Django 4.1.7 on 2023-08-28 22:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("priorities", "0002_alter_priority_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="priority",
            name="order",
            field=models.IntegerField(default=2),
        ),
    ]
