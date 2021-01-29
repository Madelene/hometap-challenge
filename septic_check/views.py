from django.http import HttpResponseRedirect
from django.shortcuts import render

from properties.property_data import PROPERTIES

from .forms import PropertyForm

# import requests


def home(request):
    # url = "https://api.housecanary.com/v2/property/details"
    # headers = {'api_key': 'fakeapikey'}
    params = {}

    if request.method == 'POST':
        form = PropertyForm(request.POST)

        if form.is_valid():
            address = request.POST.get('address')
            zipcode = request.POST.get('zipcode')

            params['address'] = address
            params['zipcode'] = zipcode

            # response = requests.get(url, headers=headers, params=params)
            # response_json = response.json()
        return HttpResponseRedirect('sewage_info')
    else:
        form = PropertyForm()

    context = {
        'sewage_system': sewage_info,
        'form': form,
    }
    return render(request, 'septic_check/home.html', context)


def sewage_info(request):
    # We would actually get the sewage_info from the response_json when making a request to the API
    sewage_info = PROPERTIES.get('property/details', {}).get('result', {}).get('property', {}).get('sewer', '')

    context = { 'sewage_system': sewage_info }
    return render(request, 'septic_check/sewage_info.html', context)
