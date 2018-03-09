# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:15 2018

@author: Liam Edelman
"""

from bs4 import BeautifulSoup
import urllib

csv = open("review.csv", "w")
csv.write("reviewID, businessID, reviewerID, date, reviewContent, rating, usefulCount, coolCount, funnyCount\n")
#reviewID
#businessID
#reviewerID
#date
#reviewContent
#rating
#usefulCount
#coolCount
#funnyCount
Page = 0

firsthalf = "https://www.yelp.com/search?find_loc=60605&start="
secondhalf = "&cflt=restaurants"
full = firsthalf + str(Page) + secondhalf

YelpPage = urllib.request.urlopen(full).read()
soup = BeautifulSoup(YelpPage, "html.parser")

resultarr = soup.find_all("li", class_="regular-search-result")
tot = 0
while(len(resultarr) != 0):
    for i in resultarr:
        address = str(i.address)
        if "60605" not in address:
            continue
        else:
            tot = tot + 1
            print(tot)
    Page = Page + 10
    full = firsthalf + str(Page) + secondhalf
    YelpPage = urllib.request.urlopen(full).read()
    soup = BeautifulSoup(YelpPage, "html.parser")
    resultarr = soup.find_all("li", class_="regular-search-result")