# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:42:26 2018

@author: Liam Edelman
"""

import json
import urllib

#What is the viability of a business, i.e., how long is a business active, after a failed food inspection?
#Restaurant Name, Address, Failed inspection on, Alive for x years

MainCrimeURL = "https://data.cityofchicago.org/resource/6zsd-86xi.json?"

Block = "024XX W OGDEN AVE"

URL = MainCrimeURL + urllib.parse.urlencode({"block" : Block})

JSON = json.load(urllib.request.urlopen(URL))

print(json.dumps(JSON, sort_keys=True, indent=4))

exit