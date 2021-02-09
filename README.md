# Septic-Check
This example web app is meant to return sewage information on a property. When calling the actual API, the address and zipcode entered by the user would be passed in as parameters to the request.
The corresponding response would return the payload that contains information about the sewage system on the property.
The `sewer` field returns one of these options: `Municipal, None, Storm, Septic, Yes`.
For our purposes, we are interested to see if the property uses Septic.

#### Details

- Python version 3.8.2
- Django version 3.1.5


#### Set up and Running the Project Locally

- Clone the files from GitHub, open the terminal, and cd into the project.

- In the root of the project, create a virtual environment: `python3 -m venv venv`
- activate the virtual environment: `source venv/bin/activate`
- Install the dependencies in your virtual env from the requirements.txt file: `pip install -r requirements.txt`

- From the home directory, run these commands:

 1. `python3 manage.py migrate` (optional)
 2. `python3 manage.py runserver`
 3. Navigate to `http://localhost:8000` or `http://127.0.0.1:8000` and fill out the form.


#### Run tests

In the home directory, run `export DJANGO_SETTINGS_MODULE=properties.settings`
Then, run `python -m pytest tests/`

You should be able to view the output:

```
================================================================ test session starts ================================================================
platform darwin -- Python 3.8.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
django: settings: properties.settings (from env)
rootdir: /Users/madelenecampos/Desktop/hometap-challenge, configfile: pytest.ini
plugins: cov-2.11.1, django-4.1.0, pythonpath-0.7.3
collected 7 items

tests/test_views.py .                                                                                                                         [ 14%]
tests/test_property_form.py .....                                                                                                             [ 85%]
tests/test_urls.py .                                                                                                                          [100%]

================================================================= 7 passed in 0.26s =================================================================
```
