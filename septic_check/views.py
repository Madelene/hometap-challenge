from django.shortcuts import render

# import requests


def home(request):
    # url = "https://api.housecanary.com/v2/property/details"
    # headers = {'api_key': 'fakeapikey'}
    # params = {}

    if request.method == 'POST':
        address = request.POST('address')
        zipcode = request.POST('zipcode')

        params['address']: address
        params['zipcode']: zipcode

    response_json = {
        "property/details": {
            "api_code_description": "ok",
            "api_code": 0,
            "result": {
                "property": {
                    "air_conditioning": "yes",
                    "attic": False,
                    "basement": "full_basement",
                    "building_area_sq_ft": 1824,
                    "building_condition_score": 5,
                    "building_quality_score": 3,
                    "construction_type": "Wood",
                    "exterior_walls": "wood_siding",
                    "fireplace": False,
                    "full_bath_count": 2,
                    "garage_parking_of_cars": 1,
                    "garage_type_parking": "underground_basement",
                    "heating": "forced_air_unit",
                    "heating_fuel_type": "gas",
                    "no_of_buildings": 1,
                    "no_of_stories": 2,
                    "number_of_bedrooms": 4,
                    "number_of_units": 1,
                    "partial_bath_count": 1,
                    "pool": True,
                    "property_type": "Single Family Residential",
                    "roof_cover": "Asphalt",
                    "roof_type": "Wood truss",
                    "site_area_acres": 0.119,
                    "style": "colonial",
                    "total_bath_count": 2.5,
                    "total_number_of_rooms": 7,
                    "sewer": "municipal",
                    "subdivision": "CITY LAND ASSOCIATION",
                    "water": "municipal",
                    "year_built": 1957,
                    "zoning": "RH1"
                },

                "assessment": {
                    "apn": "0000 -1111",
                    "assessment_year": 2015,
                    "tax_year": 2015,
                    "total_assessed_value": 1300000.0,
                    "tax_amount": 15199.86
                }
            }
        }
    }

    # response = requests.get(url, headers=headers, params=params)
    # response_json = response.json()
    sewage_info = response_json.get('property/details', {}).get('result', {}).get('property', {}).get('sewer', '')
    context = {
        'sewage_system': sewage_info
    }

    return render(request, 'septic_check/home.html', context)
