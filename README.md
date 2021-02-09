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

In the home directory, run `pytest --cov`

You should be able to view the coverage:

```
collected 7 items

tests/test_views.py .                                                                                                                         [ 14%]
tests/test_property_form.py .....                                                                                                             [ 85%]
tests/test_urls.py .                                                                                                                          [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
properties/__init__.py                    0      0   100%
properties/property_data.py               1      0   100%
properties/settings.py                   19      0   100%
properties/urls.py                        3      0   100%
septic_check/__init__.py                  0      0   100%
septic_check/admin.py                     1      0   100%
septic_check/apps.py                      3      0   100%
septic_check/forms.py                     4      0   100%
septic_check/migrations/__init__.py       0      0   100%
septic_check/models.py                    1      0   100%
septic_check/urls.py                      3      0   100%
septic_check/views.py                    21     12    43%
tests/__init__.py                         0      0   100%
tests/test_property_form.py               6      0   100%
tests/test_urls.py                        7      0   100%
tests/test_views.py                       7      0   100%
---------------------------------------------------------
TOTAL                                    76     12    84%
```
