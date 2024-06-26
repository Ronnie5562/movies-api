# Generated by Django 4.0.10 on 2024-04-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_review_content_object_review_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='bbfc_rating',
            field=models.CharField(choices=[('U', 'Universal - Suitable for all ages.'), ('PG', 'Parental Guidance - Scenes may be unsuitable for children.'), ('12', '12A/12 - Suitable for 12 years and over.'), ('15', '15 - Suitable only for 15 years and over.'), ('18', '18 - Suitable only for adults.'), ('R18', 'Restricted 18 - Only available in licensed premises'), ('E', 'Exempt - Not subject to classification.'), ('TBC', 'To Be Confirmed - Rating is yet to be determined.')], default='U', help_text='Select the BBFC rating for this movie.', max_length=4, verbose_name='BBFC Rating'),
        ),
    ]
