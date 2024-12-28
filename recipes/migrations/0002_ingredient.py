# Generated by Django 4.2.17 on 2024-12-28 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.IntegerField(default=0)),
                ('unit', models.CharField(choices=[('tsp', 'teaspoon'), ('tbsp', 'tablespoon'), ('fl oz', 'fluid ounce'), ('cup', 'cup'), ('g', 'gram'), ('kg', 'kilogram'), ('l', 'liter'), ('ml', 'milliter'), ('cm', 'centimeter')], default='g', max_length=20)),
                ('ingredient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_name', to='recipes.ingredientname')),
            ],
        ),
    ]
