# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:42:26 2018

@author: Liam Edelman
"""

import json
import urllib


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
    
    for _license in IssuedLicenses:
        if Name == _license.get('doing_business_as_name'):
            Lifespan = int(_license.get('expiration_date')[:4]) - YearFailed
            csv.write(Name + "," + Address + "," + Date + "," + str(Lifespan) + "\n")
            break

csv.close()
    
    
    
    
    
    
    
    
    
    
    
    