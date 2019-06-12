# Generated by Django 2.2.2 on 2019-06-12 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_platform', '0004_auto_20190612_1056'),
        ('get_course', '0002_auto_20190612_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interTable', to='get_course.CourseOverview')),
                ('platforms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interTable', to='get_platform.IntegratedPlatforms')),
            ],
        ),
        migrations.AddField(
            model_name='courseoverview',
            name='platforms',
            field=models.ManyToManyField(blank=True, related_name='courses', through='get_course.GroupMember', to='get_platform.IntegratedPlatforms'),
        ),
    ]