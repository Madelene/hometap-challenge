# Septic-Check
This example web app is meant to return sewage information on a property. When actually calling the API, the address and zipcode entered by the user would be passed in as parameters to the request.
The corresponding response would return the payload that contains information about the sewage system on the property.
The `sewer` field returns one of these options: `Municipal, None, Storm, Septic, Yes`.
For our purposes, we are interested to see if the property uses Septic.

#### Set up and Running the Project Locally

- Python version 3.8.2
- Django version 3.1.5

- Clone the files from GitHub, open the terminal, and cd into the project.

- In the root of the project, create a virtual environment: `python3 -m venv venv`
- activate the virtual environment: `source venv/bin/activate`
- Install the dependencies in your virtual env from the requirements.txt file: `pip install -r requirements.txt`

- From the home directory, run these commands:

 1. `python3 manage.py migrate` (optional)
 2. `python3 manage.py runserver`
 3. Navigate to `http://localhost:8000` or `http://127.0.0.1:8000` and fill out the form.


#### Run tests

Simply run `pytest` from the project directory. You should be able to view the full test coverage:
```
collected 7 items

septic_check/tests/test_views.py::test_sewage_info_passing PASSED                                                                             [ 14%]
septic_check/tests/test_property_form.py::test_example_form[123 S. Main St-92357-True] PASSED                                                 [ 28%]
septic_check/tests/test_property_form.py::test_example_form[33457-12345678910-False] PASSED                                                   [ 42%]
septic_check/tests/test_property_form.py::test_example_form[55 East Washington-None-False] PASSED                                             [ 57%]
septic_check/tests/test_property_form.py::test_example_form[-18-False] PASSED                                                                 [ 71%]
septic_check/tests/test_property_form.py::test_example_form[None-18-False] PASSED                                                             [ 85%]
septic_check/tests/test_urls.py::test_urls PASSED                                                                                             [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                                       Stmts   Miss  Cover
--------------------------------------------------------------
manage.py                                     12     12     0%
properties/__init__.py                         0      0   100%
properties/asgi.py                             4      4     0%
properties/property_data.py                    1      0   100%
properties/settings.py                        19      0   100%
properties/urls.py                             3      0   100%
properties/wsgi.py                             4      4     0%
septic_check/__init__.py                       0      0   100%
septic_check/admin.py                          1      0   100%
septic_check/apps.py                           3      0   100%
septic_check/forms.py                          4      0   100%
septic_check/migrations/__init__.py            0      0   100%
septic_check/models.py                         1      0   100%
septic_check/tests/__init__.py                 0      0   100%
septic_check/tests/test_property_form.py       6      0   100%
septic_check/tests/test_urls.py                7      0   100%
septic_check/tests/test_views.py               7      0   100%
septic_check/urls.py                           3      0   100%
septic_check/views.py                         21     12    43%
--------------------------------------------------------------
TOTAL                                         96     32    67%

```
