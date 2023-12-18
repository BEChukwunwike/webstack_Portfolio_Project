# Generated by Django 5.0 on 2023-12-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image_filter",
            field=models.CharField(
                choices=[
                    ("_2023", "2023"),
                    ("ausconnect", "Australia"),
                    ("brconnect", "Brazil"),
                    ("canconnect", "Canada"),
                    ("chnconnect", "China"),
                    ("egconnect", "Egypt"),
                    ("franceconnect", "France"),
                    ("gerconnect", "Germany"),
                    ("grcconnect", "Greece"),
                    ("indconnect", "India"),
                    ("indonconnect", "Indonesia"),
                    ("itaconnect", "Italy"),
                    ("jpsconnect", "Japan"),
                    ("kconnect", "Korea"),
                    ("mexconnect", "Mexico"),
                    ("9jaconnect", "Nigeria"),
                    ("rusconnect", "Russia"),
                    ("saconnect", "South Africa"),
                    ("spnconnect", "Spanish"),
                    ("thnconnect", "Thailand"),
                    ("turkconnect", "Turkey"),
                    ("uaeconnect", "UAE"),
                    ("ukconnect", "UK"),
                    ("usaconnect", "USA"),
                ],
                default="_2023",
                max_length=100,
            ),
        ),
    ]
