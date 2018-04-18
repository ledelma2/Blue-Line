# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:42:26 2018

@author: Liam Edelman
"""

import json
import urllib
from collections import namedtuple


#Example of data.cityofchicago API
# =============================================================================
# MainCrimeURL = "https://data.cityofchicago.org/resource/6zsd-86xi.json?"
#
# Block = "024XX W OGDEN AVE"
#
# URL = MainCrimeURL + urllib.parse.urlencode({"block" : Block})
#
# JSON = json.load(urllib.request.urlopen(URL))
#
# print(json.dumps(JSON, sort_keys=True, indent=4))
# =============================================================================

#Example of SoQL URL Parsing
# =============================================================================
# MainCrimeURL = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=beat%20=%20%271023%27&$select=beat,block&$order=block%20ASC&$limit=50000"
# 
# URL = MainCrimeURL
# 
# JSON = json.load(urllib.request.urlopen(URL))
# 
# print(json.dumps(JSON, sort_keys=True, indent=4))
# =============================================================================

#Example of census.gov GeoCoder API
# =============================================================================
# MainCensusURL = "https://geocoding.geo.census.gov/geocoder/geographies/address?street=1250+South+Halsted+St&zip=60607&benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=14&format=json"
#  
# URL = MainCensusURL
#  
# JSON = json.load(urllib.request.urlopen(URL))
#  
# print(json.dumps(JSON, sort_keys=True, indent=4))
# =============================================================================

#What is the viability of a business, i.e., how long is a business active, after a failed food inspection?
#Restaurant Name, Address, Failed inspection on, Alive for x years

InspectionURL = "https://data.cityofchicago.org/resource/cwig-ma7x.json?$select=inspection_date,address,dba_name&$where=results=%27Fail%27%20AND%20zip%20%3C%2060608%20AND%20zip%20%3E%2060600&$order=inspection_date%20ASC&$limit=50000"
LicenseURL = "https://data.cityofchicago.org/resource/xqx5-8hwx.json?$select=expiration_date,doing_business_as_name&$where=zip_code%20%3E%20%2760600%27%20AND%20zip_code%20%3C%20%2760608%27&$order=expiration_date%20DESC&$limit=100000"
FailedInspections = json.load(urllib.request.urlopen(InspectionURL))
IssuedLicenses = json.load(urllib.request.urlopen(LicenseURL))

csv = open("query8.csv", "w")
csv.write("Name, Address, Failed inspection on, Alive for x years\n")



for entry in FailedInspections:
    Name = entry.get('dba_name')
    Address = entry.get('address')
    Date = entry.get('inspection_date')
    YearFailed = int(Date[:4])
    
    for license1 in IssuedLicenses:
        if Name == license1.get('doing_business_as_name'):
            Lifespan = int(license1.get('expiration_date')[:4]) - YearFailed
            csv.write(Name + "," + Address + "," + Date + "," + str(Lifespan) + "\n")
            break

csv.close()
    
#Does having a liquor license influence crime incidents in the neighborhood?
#Census Block, # of Businesses with liquor licenses, # of Crimes, # of Arrests

CrimeURL = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$select=block,%20arrest&$where=date%20%3E%20%272016-01-01T00:00:00.000%27&$order=block%20DESC"
LicenseURL = "https://data.cityofchicago.org/resource/nrmj-3kcf.json?$select=address,%20zip_code,%20expiration_date&$where=(zip_code%20%3E%20%2760600%27%20AND%20zip_code%20%3C%20%2760608%27)%20AND%20(business_activity_id=%27638%27%20OR%20business_activity_id=%27774%27%20OR%20business_activity_id=%27829%27)%20AND%20(expiration_date%20%3E%20%272018-04-17T00:00:00.000%27)&$order=address%20DESC"
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

    
    
    
    
    
    
    
    
    