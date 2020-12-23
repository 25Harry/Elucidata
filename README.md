# Elucidata

> Flask Server to process excel file and return sorted versions

## Getting Started

```sh

# Setting up virtual environment for local development
virtualenv -p python3 venv

# Activate the virtual environment
./venv/Scripts/activate

# Install dependencies
pip3 install -r requirements.txt

# Set flask environment variables
set FLASK_APP=app.py
set FLASK_ENV=development

# Run flask server locally
flask run

```

## Endpoints 

- ### `POST /`
        home page opened where you have to upload file.
- ### `POST /upload`
        This will show the uploaded file.
- ### `POST /filter`
        This will filter out all the data for metabolite ids ending with:‘PC’, ‘LPC’ and ‘plasmalogen’, and create 3 child datasets
        (1 for each compound id) from the data in input file as-
        - LC.xlsx
        - LPC.xlsx
        - plasmalogen.xlsx
        Also download them after completion of backend process.
- ### `POST /roundoff`
        This will add a new column in the parent dataset with the name “Retention Time Roundoff (in mins)”. This column should have 
        rounded-off values of the corresponding retention time. Retention time should be rounded-off to the nearest natural number.
        Download the file roundoff.xlsx after completeion of backend process.
 - ### `POST /mean`
        This will find the mean of all the metabolites according to condition provided
        Download the file mean.xlsx after completion of backend process
        
        
    
