from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from myapp.choices import CAM_CHOICES, CAMERA_NUMBER, VIDEO_TYPE


def upload_to_video_app(instance, filename):
    name, ext = filename.split('.')
    file_path = 'videos/offline_Videos/{}/{}/{}/{}/{}/{}/{}.{}'.format(instance.location.area.city.state.country,
                                                                       instance.location.area.city.state,
                                                                       instance.location.area.city,
                                                                       instance.location.area,
                                                                       instance.location.sub_location,
                                                                       instance.location.camera_number, name, ext)
    return file_path


class Country(models.Model):
    country = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return self.state


class City(models.Model):
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return self.city


class Area(models.Model):
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return self.area


class Video_Type(models.Model):
    video_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return self.video_type


class Domain_Type(models.Model):
    domain_type = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    video_type = models.ForeignKey(Video_Type, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.domain_type) + '-' + str(self.video_type) + '-' + str(self.description)


class Location(models.Model):
    area = models.ForeignKey(Area, on_delete='CASCADE')
    sub_location = models.IntegerField(choices=CAM_CHOICES, default=1)
    camera_number = models.IntegerField(choices=CAMERA_NUMBER, default=1)
    description = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    domain_type = models.ForeignKey(Domain_Type, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.area) + '-' + str(self.sub_location) + '-' + str(self.camera_number)


class Camera_API(models.Model):
    api_name = models.CharField(max_length=100)
    use_case = models.CharField(max_length=100)
    api_url = models.URLField()
    location = models.ForeignKey(Location, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.api_name) + '-' + str(self.use_case) + '-' + str(self.location)


class Scripts(models.Model):
    scripts_name = models.CharField(max_length=100)
    scripts = models.FileField()
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.scripts_name) + '-' + str(self.scripts)


class Camera_API_Scripts(models.Model):
    camera_api_scripts_name = models.CharField(max_length=100)
    camera_api = models.ForeignKey(Camera_API, on_delete='CASCADE')
    scripts = models.ForeignKey(Scripts, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.camera_api) + '-' + str(self.scripts)


class Video_Input(models.Model):  # index of all 3 fields are different
    video_input = models.FileField()
    video_input_test = models.FileField()
    from_date_time = models.DateTimeField()
    to_date_time = models.DateTimeField()
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.video_input) + '-' + str(self.video_input_test)


class Camera_API_On_Video_Input(models.Model):
    camera_api_on_video_input_name = models.CharField(max_length=100)
    camera_api = models.ForeignKey(Camera_API, on_delete='CASCADE')
    video_input = models.ForeignKey(Video_Input, on_delete='CASCADE')
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.camera_api_on_video_input_name) + '-' + str(self.camera_api) + '-' + str(self.video_input)


class AI_Use_Case_Occurrence(models.Model):
    video_output = models.FileField()
    video_output_test = models.FileField()
    camera_api_on_video_input = models.ForeignKey(Camera_API_On_Video_Input, on_delete='CASCADE')
    from_date_time = models.DateTimeField()
    to_date_time = models.DateTimeField()
    user = models.ForeignKey(User, null=True, on_delete='CASCADE')

    def __str__(self):
        return str(self.video_output) + '-' + str(self.video_output_test) + '-' + str(
            self.camera_api_on_video_input) + '-' + str(self.from_date_time) + '-' + str(self.to_date_time)
