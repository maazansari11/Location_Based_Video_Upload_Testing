import json
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.forms import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration_form.html', {'form': form})


def poc_display(request):
    return redirect('poc1')


def video_type(request):
    print("this is another test")
    onofftoggle = Video_Type.objects.all()
    return render(request, 'video_type.html', {'onofftoggle': onofftoggle})


def video_type_details(request, online_offline_video):
    print(online_offline_video)
    _online_offline_video = int(online_offline_video)
    onofftoggle = Video_Type.objects.filter(id=_online_offline_video)
    domain_type = Domain_Type.objects.filter(video_type_id=_online_offline_video)
    context = {
        'onofftoggle': onofftoggle,
        'domain_type': domain_type
    }
    return render(request, 'video_type_details.html', context)


def domain_type(request, online_offline_video):
    print(online_offline_video)
    onofftoggle = Video_Type.objects.filter(id=online_offline_video)
    domain_type = Domain_Type.objects.filter(video_type_id=online_offline_video)
    print(domain_type)
    context = {
        'onofftoggle': onofftoggle,
        'domain_type': domain_type
    }
    return render(request, 'domain_type.html', context)


def domain_type_details(request, online_offline_video, domain_type):
    domain_type_list = Domain_Type.objects.filter(video_type_id=online_offline_video)
    country_list = load_country_list(domain_type)
    locations = Location.objects.filter(domain_type_id=domain_type)
    print(locations)
    context = {
        'country_list': country_list,
        'locations': locations,
        'domain_type_id': domain_type,
        'domain_type': domain_type_list,
        'online_offline_video_id': online_offline_video,
    }
    return render(request, 'domain_type_details.html', context)


def load_country_list(domain_type):
    country_list = []
    locations = Location.objects.filter(domain_type_id=domain_type)
    print(locations[0].area)
    for l in locations:
        country = Country.objects.filter(id=l.area.city.state.country.id)
        print(country[0])
        country_data = {"country_id": country[0].id, "country": country[0].country}
        print(country_data)
        country_list.append(country_data)
        print(country_list)
    country_list_json = json.dumps(country_list)
    print('after for loop ', country_list)
    return country_list


def load_state_list(domain_type, country):
    state_list = []
    locations = Location.objects.filter(domain_type_id=domain_type)
    print(locations[0].area)
    for l in locations:
        states = State.objects.filter(id=l.area.city.state.id)
        for state in states:
            print(domain_type)
            print(country)
            print(state.country.id)

            if int(country) == int(state.country.id):
                state_data = {"state_id": state.id, "state": state.state}
                print(state_data)
                state_list.append(state_data)
                print(state_list)
    state_list_json = json.dumps(state_list)
    print('after for loop ', state_list)
    return state_list


def load_city_list(domain_type, country, state):
    city_list = []
    locations = Location.objects.filter(domain_type_id=domain_type)
    print(locations[0].area)
    for l in locations:
        cities = City.objects.filter(id=l.area.city.id)
        for city in cities:
            print(domain_type)
            print(country)
            print(state)
            print(city.state.country.id)

            if int(city) == int(city.state.country.id):
                city_data = {"city_id": city.id, "city": city.city}
                print(city_data)
                city_list.append(city_data)
                print(city)
    city_list_json = json.dumps(city_list)
    print('after for loop ', city_list)
    return city_list


def load_countries(request, domain_type):
    country_list = []
    final_list = []
    locations = Location.objects.filter(domain_type_id=domain_type)
    print(locations[0].area)
    for l in locations:
        country = Country.objects.filter(id=l.area.city.state.country.id)
        print(country[0])
        country_data = {"country_id": country[0].id, "country": country[0].country}
        print(country_data)
        country_list.append(country_data)
        print(country_list)
    # country_list_json = json.dumps(country_list)
    print('after for loop ', country_list)
    for num in country_list:
        if num not in final_list:
            final_list.append(num)
    print("Final list", final_list)
    return render(request, 'countries_dropdown_list_options.html', {'country_list': final_list})


def load_states(request, domain_type_id, country_id):
    print("this is test print")
    state_list = load_state_list(domain_type_id, country_id)
    print("in load_states function ", state_list)
    return render(request, 'state_dropdown_list_options.html', {'state_list': state_list})


def load_cities(request, domain_type_id, country_id, state_id):
    city_list = load_city_list(domain_type_id, country_id, state_id)
    print("in load_states function ", city_list)
    return render(request, 'city_dropdown_list_options.html', {'city_list': city_list})


def load_areas(request):
    city_id = request.GET.get('city')
    areas = Area.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'area_dropdown_list_options.html', {'areas': areas})


def location(request, **kwargs):
    keys_list = []
    values_list = []
    print("kwargs")
    print(kwargs)
    for key, value in kwargs.items():
        keys_list.append(key)
        values_list.append(value)
    if 6 >= len(values_list) > 1:
        if len(values_list) == 2:
            online_offline_video = values_list[0]
            domain_type = values_list[1]
            locations = Location.objects.filter(domain_type_id=domain_type)
            context = {
                'locations': locations,
                'online_offline_video': online_offline_video,
                'domain_type_id': domain_type,
            }
        elif len(values_list) == 3:
            online_offline_video = values_list[0]
            domain_type = values_list[1]
            country_id = values_list[2]
            states = State.objects.filter(country_id=country_id)
            cities = City.objects.filter(state_id__in=states)
            areas = Area.objects.filter(city_id__in=cities)
            locations = Location.objects.filter(domain_type_id=domain_type, area_id__in=areas)
            context = {
                'country_id': country_id,
                'locations': locations,
                'online_offline_video': online_offline_video,
                'domain_type_id': domain_type,
            }
        elif len(values_list) == 4:
            online_offline_video = values_list[0]
            domain_type = values_list[1]
            country_id = values_list[2]
            state_id = values_list[3]
            cities = City.objects.filter(state_id=state_id)
            areas = Area.objects.filter(city_id__in=cities)
            locations = Location.objects.filter(domain_type_id=domain_type, area_id__in=areas)
            context = {
                'country_id': country_id,
                'state_id': state_id,
                'locations': locations,
                'online_offline_video': online_offline_video,
                'domain_type_id': domain_type,
            }
        elif len(values_list) == 5:
            online_offline_video = values_list[0]
            domain_type = values_list[1]
            country_id = values_list[2]
            state_id = values_list[3]
            city_id = values_list[4]
            areas = Area.objects.filter(city_id=city_id)
            locations = Location.objects.filter(domain_type_id=domain_type, area_id__in=areas)
            context = {
                'country_id': country_id,
                'state_id': state_id,
                'city_id': city_id,
                'locations': locations,
                'online_offline_video': online_offline_video,
                'domain_type_id': domain_type,
            }
        elif len(values_list) == 6:
            online_offline_video = values_list[0]
            domain_type = values_list[1]
            country_id = values_list[2]
            state_id = values_list[3]
            city_id = values_list[4]
            area_id = values_list[5]
            locations = Location.objects.filter(domain_type_id=domain_type, area_id=area_id)
            context = {
                'country_id': country_id,
                'state_id': state_id,
                'city_id': city_id,
                'area_id': area_id,
                'locations': locations,
                'online_offline_video': online_offline_video,
                'domain_type_id': domain_type,
            }

    return render(request, 'location_filter_table.html', context)


# def location_details(request, online_offline_video, domain_type, country, state):
#     onofftoggle = Video_Type.objects.filter(id=online_offline_video)
#     _domain_type = Domain_Type.objects.filter(video_type_id=online_offline_video)
#     location = Location.objects.filter(domain_type_id=domain_type)
#     location_country = Location.objects.filter(domain_type_id=domain_type,
#                                                country_id=country)
#     location_state = Location.objects.filter(domain_type_id=domain_type,
#                                              country_id=country, state_id=state)
#     context = {
#         'onofftoggle': onofftoggle,
#         'domain_type': _domain_type,
#         'location': location,
#         'location_area': location_country,
#         'location_state': location_state,
#     }
#     return render(request, 'location_details.html', context)


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("uploaded successfully")
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})
