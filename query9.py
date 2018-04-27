# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:06:47 2018

@author: Liam Edelman
"""

import json
import urllib

#Does having a liquor license influence crime incidents in the neighborhood?
#Census Block, # of Businesses with liquor licenses, # of Crimes, # of Arrests

CrimeURL = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$select=block,%20arrest&$where=date%20%3E%20%272016-01-01T00:00:00.000%27&$order=block%20DESC&$limit=100000"
LicenseURL = "https://data.cityofchicago.org/resource/nrmj-3kcf.json?$select=address,%20zip_code,%20expiration_date&$where=(zip_code%20%3E%20%2760600%27%20AND%20zip_code%20%3C%20%2760608%27)%20AND%20(business_activity_id=%27638%27%20OR%20business_activity_id=%27774%27%20OR%20business_activity_id=%27829%27)%20AND%20(expiration_date%20%3E%20%272018-04-17T00:00:00.000%27)&$order=address%20DESC&$limit=50000"
LiquorLicenses = json.load(urllib.request.urlopen(LicenseURL))
CrimeReports = json.load(urllib.request.urlopen(CrimeURL))

csv = open("query9.csv", "w")
csv.write("Census Block, # of Businesses with liquor licenses, # of Crimes, # of Arrests\n")

MainCensusURL = "https://geocoding.geo.census.gov/geocoder/geographies/address?"
SecondaryCensusURL = "&benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=14&format=json"


BlockList = []

for i in range (0, 5000):
    BlockList.append([0, 0, 0])
    

for license1 in LiquorLicenses: 
    address = license1.get('address')
    zip1 = license1.get('zip_code')
      
    URL = MainCensusURL + urllib.parse.urlencode({'street': address}) + '&' + urllib.parse.urlencode({'zip': zip1}) + SecondaryCensusURL
      
    StreetData = json.load(urllib.request.urlopen(URL))
    String = str(StreetData.get('result').get('addressMatches'))
    i = String.find('BLOCK')
    Block = String[i + 9:i + 13].strip()

    if Block != '':    
        BlockNo = int(Block)
        BlockList[BlockNo][0] = BlockList[BlockNo][0] + 1
            
        for crimes in CrimeReports:
            block = crimes.get('block')
            i = block.find('XX')
            number = block[:i]
            street = block[i + 3:]
            if address.find(street) > 0:
                BlockList[BlockNo][1] = BlockList[BlockNo][1] + 1
                if crimes.get('arrest') == True:
                    BlockList[BlockNo][2] = BlockList[BlockNo][2] + 1
                
for c in range (0, 5000):
    if BlockList[c] != [0, 0, 0]:
        csv.write(str(c) + ',' + str(BlockList[c][0]) + ',' + str(BlockList[c][1]) + ',' + str(BlockList[c][2]) + '\n')
        
csv.close()