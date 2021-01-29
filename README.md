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
