# Generated by Django 2.1.11 on 2019-08-19 07:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AI_Use_Case_Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_output', models.FileField(upload_to='')),
                ('video_output_test', models.FileField(upload_to='')),
                ('from_date_time', models.DateTimeField()),
                ('to_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Camera_API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100)),
                ('use_case', models.CharField(max_length=100)),
                ('api_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Camera_API_On_Video_Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_api_on_video_input_name', models.CharField(max_length=100)),
                ('camera_api', models.ForeignKey(on_delete='CASCADE', to='myapp.Camera_API')),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Camera_API_Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camera_api_scripts_name', models.CharField(max_length=100)),
                ('camera_api', models.ForeignKey(on_delete='CASCADE', to='myapp.Camera_API')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Domain_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_type', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_location', models.IntegerField(choices=[(1, 'FRONT'), (2, 'BACK')], default=1)),
                ('camera_number', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1)),
                ('description', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=10)),
                ('area', models.ForeignKey(on_delete='CASCADE', to='myapp.Area')),
                ('domain_type', models.ForeignKey(on_delete='CASCADE', to='myapp.Domain_Type')),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scripts_name', models.CharField(max_length=100)),
                ('scripts', models.FileField(upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete='CASCADE', to='myapp.Country')),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_input', models.FileField(upload_to='')),
                ('video_input_test', models.FileField(upload_to='')),
                ('from_date_time', models.DateTimeField()),
                ('to_date_time', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_type', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='domain_type',
            name='video_type',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.Video_Type'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.State'),
        ),
        migrations.AddField(
            model_name='city',
            name='user',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='camera_api_scripts',
            name='scripts',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.Scripts'),
        ),
        migrations.AddField(
            model_name='camera_api_scripts',
            name='user',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='camera_api_on_video_input',
            name='video_input',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.Video_Input'),
        ),
        migrations.AddField(
            model_name='camera_api',
            name='location',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.Location'),
        ),
        migrations.AddField(
            model_name='camera_api',
            name='user',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.City'),
        ),
        migrations.AddField(
            model_name='area',
            name='user',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ai_use_case_occurrence',
            name='camera_api_on_video_input',
            field=models.ForeignKey(on_delete='CASCADE', to='myapp.Camera_API_On_Video_Input'),
        ),
        migrations.AddField(
            model_name='ai_use_case_occurrence',
            name='user',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
