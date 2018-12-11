# Generated by Django 2.1.2 on 2018-11-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('match_score', models.FloatField(blank=True, null=True)),
                ('listing_url', models.TextField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('accommodates', models.IntegerField()),
                ('guests_included', models.IntegerField()),
                ('extra_people', models.IntegerField()),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('beds', models.IntegerField(blank=True, null=True)),
                ('neighborhood', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('minimum_nights', models.IntegerField()),
                ('maximum_nights', models.IntegerField()),
            ],
            options={
                'db_table': 'listing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('listing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_for_stay', models.DateField()),
                ('available', models.CharField(max_length=1)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'offering',
                'managed': False,
            },
        ),
    ]