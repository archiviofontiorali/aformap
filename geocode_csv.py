# -*- coding: utf-8 -*-
import csv
import re
import geocoder
import time
import itertools

'''
The script assumes that the .csv file (derived from the Google Form spreadsheet v0.1) is structured as with the new "0.1" format, i.e.:
column A = "Timestamp" (date and time of when the questionnaire was filled in)
B = "Your name"
C = "Your surname"
D = "Describe yourself in one tweet (No more than 280 characters)"
E = "Where are you from (country) / which country do you consider "home"?"
F = "Add a profile picture"
G = "Country"
H = "City"
I = "Street name"
J = "Number"
K = "Skill #1"
L = "Skill #2"
M = "Skill #3"
N = "Skill #4"
O = "Skill #5"
P = "Language skills (if multiple "Other", separate them with a semicolon)"
Q = "Facebook (insert the link to your profile or page) MAX 1"
R = "Twitter (insert the link to your profile or page) MAX 1"
S = "Instagram (insert the link to your profile or page) MAX 1"
T = "Website (insert the link to your profile or page) MAX 1"
'''

######################################
#   MANUAL CONFIGURATION
######################################

#Change the input filename so that it matches the .csv file of the spreadsheet
input_file = ('nodes.csv')

output_file = open('nodes_geotagged.csv', 'a')
writer = csv.writer(output_file)
writer.writerow(['utteredby','name','fullname','id','address','descr','lat','lon','ialink'])

#Start reading the csv file
with open(input_file, 'r', newline='') as input_file:
    #file_output = pygeoj.new()
    readcsv = csv.reader(input_file, delimiter='\t', quotechar='"')
    prog_number = itertools.count()

    # Skip the first row, containing the header
    next(readcsv)
    rows = [r for r in readcsv]
    for row in rows:
        gform_from = row[0]
        gform_name = row[1].capitalize()
        gform_id = row[2]
        gform_address = row[3]
        gform_description = row[4]
        gform_lat = row[5]
        gform_lon = row[6]
        gform_ialink = row[7]
        #print('Collecting details for *** ' + '\x1b[31;3m' + gform_name + ' ' + gform_surname + '\x1b[0m' + ' ***')

#Translate the address into lon and lat coordinates using Google API (OSM could not cope with partial addresses such as the one many wisers wrote);
#Wait 3 seconds after each query, to avoid misusing the API
        print(gform_address)
        if len(gform_address) > 4:
           req_address = geocoder.osm(str(gform_address))
           coord_address = req_address.latlng
           print(coord_address)
           
           if coord_address is not None:
              gform_lon = coord_address[0]
              gform_lat = coord_address[1]
         
           else:
              gform_lon = 'NotAvailable'
              gform_lat = 'NotAvailable'
           time.sleep(5)
        
        else:
           gform_lon = 'NotAvailable'
           gform_lat = 'NotAvailable'
        
        
        
        print([gform_from, gform_name, gform_id, gform_address, gform_description, gform_lat, gform_lon, gform_ialink])
        
        with open('nodes_geotagged.csv', mode='a') as output_file:
           writer = csv.writer(output_file, delimiter = '\t')
           writer.writerow([gform_from, gform_name, gform_id, gform_address, gform_description, gform_lat, gform_lon, gform_ialink])

