# Generated by Django 4.2.17 on 2025-01-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_alter_recipe_other_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='other_ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
