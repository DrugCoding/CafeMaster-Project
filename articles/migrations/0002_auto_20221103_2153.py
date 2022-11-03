# Generated by Django 3.2.13 on 2022-11-03 12:53

from django.conf import settings
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='lastorder',
        ),
        migrations.AddField(
            model_name='cafe',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarksuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cafe',
            name='map_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cafe',
            name='picture1',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='picture2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='picture3',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(related_name='likeuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
