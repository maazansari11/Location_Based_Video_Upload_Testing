from django import forms
from myapp.models import *


class Country_Form(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country']


class State_Form(forms.ModelForm):
    class Meta:
        model = State
        fields = ['state']


class City_Form(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']


class Area_Form(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['area']


class Sub_Location_Form(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['sub_location']


class Video_Type_Form(forms.ModelForm):
    class Meta:
        model = Video_Type
        fields = ['video_type']


class Domain_Type_Form(forms.ModelForm):
    class Meta:
        model = Domain_Type
        fields = ['domain_type', 'description', 'video_type']


class Location_Form(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['area', 'sub_location', 'camera_number', 'description', 'latitude', 'longitude', 'domain_type']


class Camera_API_Form(forms.ModelForm):
    class Meta:
        model = Camera_API
        fields = ['api_name', 'use_case', 'api_url', 'location']


class Scripts_Form(forms.ModelForm):
    class Meta:
        model = Scripts
        fields = ['scripts_name', 'scripts']


class Camera_API_Scripts_Form(forms.ModelForm):
    class Meta:
        model = Camera_API_Scripts
        fields = ['camera_api_scripts_name', 'camera_api', 'scripts']


class Video_Input_Form(forms.ModelForm):
    class Meta:
        model = Video_Input
        fields = ['video_input', 'video_input_test', 'from_date_time', 'to_date_time']


class Camera_API_On_Video_Input_Form(forms.ModelForm):
    class Meta:
        model = Camera_API_On_Video_Input
        fields = ['camera_api_on_video_input_name', 'camera_api', 'video_input']


class AI_use_case_Occurrence_Form(forms.ModelForm):
    class Meta:
        model = AI_Use_Case_Occurrence
        fields = ['video_output', 'video_output_test', 'camera_api_on_video_input', 'from_date_time', 'to_date_time']
