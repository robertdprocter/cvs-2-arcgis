# Import modules
# Time used to manage looping of the cycle
from time import sleep
# Requests used to access API
import requests
# Pandas used to handle data in a dataframe and convert to CSV
import pandas as pd
#from io import StringIO
import os
import sys
# Convertbng to convert British National Grid to decimal longitude and latitude.
import convertbng
from convertbng.util import convert_bng, convert_lonlat
# Arcgis to update feature layer
import arcgis

# API credentials here
clientID = 'Put your own here'
clientSecret = 'Put your own here'

print('()==============================================================()')
print('|            Arcpublish 1.0: Feature layer updater               |')
print('()==============================================================()')
print('| Authored and maintained by Robert Procter     GPL-3.0 license  |')
print('|                                                                |')
print('| Check the GitHub at:                                           |')
print('| https://github.com/robertdprocter/cvs-2-arcgis                 |')
print('()==============================================================()')

# PART 1: FETCH DATA FROM API, based on code snippet from Thames Water API
# Modify this url to access the different end points. e.g. replace DischargeCurrentStatus at the end of the resource URL
api_root = 'https://prod-tw-opendata-app.uk-e1.cloudhub.io'
api_resource = '/data/STE/v1/DischargeCurrentStatus'
url = api_root + api_resource

# Query parameters if using them e.g. date filters, leave as '' for none, per Thames Water's suggestion.
params = '' 

# Make request
r = requests.get(url, headers={'client_id':clientID, 'client_secret': clientSecret}, params=params)
print("Requesting from " + r.url)

# Check response code, reject if not valid, otherwise populate dataframe.
if r.status_code == 200:
    response = r.json()
    df = pd.json_normalize(response, 'items')
    print()
    print('Dataframe populated successfully')
else:
    raise Exception("Request failed with status code {0}, and error message: {1}".format(r.status_code, r.json()))



# PART 2: CONVERT DATA INTO AN ACCEPTABLE CSV
# Return contextual info
print('Entries/Indexes in dataframe: ',(len(df.index)))
print('Fields/Columns in dataframe: ',(len(df.columns)))
print()


# Rename column names, ArcGIS module to publish online requires them to be under 10 characters for csv files.
print('Converting column names...')
df = df.rename(columns={'LocationName':'Name', 'PermitNumber':'PermitNo', 'LocationGridRef':'GridRef', 'ReceivingWaterCourse':'IntoWater', 'AlertStatus':'Alert',
                        'StatusChange': 'Changed', 'AlertPast48Hours':'48Hours', 'MostRecentDischargeAlertStart':'LastStart', 'MostRecentDischargeAlertStop':'LastStop'})
print('Successfully converted column names')
print()


# Convert British National Grid coordinates to decimal longitude and latitude
print('Converting British National Grid coords to decimal long and lat coords...')
df[['X', 'Y']] = df[['X', 'Y']].astype(float)
for i in df.index:
    #print(df["NAME"][i])
    x_list = [df["X"][i]]
    y_list = [df["Y"][i]]
    converted_list = convert_lonlat(x_list, y_list)
    x_cord = sum(converted_list[0])
    y_cord = sum(converted_list[1])
    df.at[i,"X"] = x_cord
    df.at[i,"Y"] = y_cord
    #print(df["X"][i])
    #print(df["Y"][i])
print('Successfully converted coordinates')
print()
    

# Generate CSV File
path = r"Make this the path of your new csv"
df.to_csv(path, index=False)
print('Generated new csv file')
print()



# PART 3: PUBLISH THE DATA INTO A SPECIFIC ARCGIS HOSTED FEATURE LAYER

# Set ArcGIS access with address and credentials: Use your own ArcGIS Online details
gis = arcgis.GIS("https://USER.maps.arcgis.com/home/", "USERNAME", "PASSWORD", verify_cert=False)
# Set id of the feature layer: Use the pre-published feature layer
csv = gis.content.get('replace this with your page id')
print('ArcGIS accessed')
# Find the existing hosted csv: Make sure the string is the name of CSV, same as the feature layer
existing_table = gis.content.search("CSV name.csv")
print('Identified existing csv')
# Delete said existing hosted csv
for item in existing_table:
    item.delete()
# Identify new csv to be updated, the most recently generated on the machine: Make this the path of the new csv
new_csv = gis.content.add({}, data= r"Path to find the new .csv")
print('Identified new csv')
# Set item properties to be changed, this will be updated to include a timestamp.
item_prop = {'title':'DischargeStatus'}
print('Updating layer...')
new_csv.update(item_properties = item_prop)
# Publish the changes
new_csv.publish(overwrite=True)
# Confirm success
print('Successfully updated layer')

#Kill program to end
