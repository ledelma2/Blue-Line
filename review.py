# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:15 2018

@author: Liam Edelman
"""

from bs4 import BeautifulSoup
import urllib

csv = open("review.csv", "w")
csv.write("reviewID, businessID, reviewerID, date, reviewContent, rating, usefulCount, coolCount, funnyCount\n")
reviewID = ""
businessID = ""
reviewerID = ""
date = ""
reviewContent = ""
rating = ""
usefulCount = ""
coolCount = ""
funnyCount = ""
Page = 0

firsthalf = "https://www.yelp.com/search?find_loc=60605&start="
secondhalf = "&cflt=restaurants"
full = firsthalf + str(Page) + secondhalf

YelpPage = urllib.request.urlopen(full).read()
soup = BeautifulSoup(YelpPage, "html.parser")

resultarr = soup.find_all("li", class_="regular-search-result")


while(len(resultarr) != 0):
    
    for i in resultarr:
        
        address = str(i.address)
        
        if "60605" not in address:
            continue
            
        else:
            a = str(resultarr[0].find("a", class_="biz-name js-analytics-click"))
            i1 = a.find("biz/")
            i2 = a.find("True\"")
            res1st = "https://www.yelp.com"
            res2nd = a[i1 - 1:i2 + 4]
            res3rd = "?start="
            respage = 0
            res4th = "&sort_by=date_asc"
            resfull = res1st + res2nd + res3rd + str(respage) + res4th
            businessID = a[i1 + 4: i2 - 6]

            RestaurantPage = urllib.request.urlopen(resfull).read()
            RestaurantSoup = BeautifulSoup(RestaurantPage, "html.parser")

            Reviews = RestaurantSoup.find_all("div", class_="review review--with-sidebar")

            while(len(Reviews) != 0):
                for a in Reviews:
                    userTag = a.find("a", class_="user-display-name")
                    i1 = str(userTag).find("name\"")
                    i2 = str(userTag).find("</a>")
                    reviewerID = str(userTag)[i1 + 6:i2]
                    
                    i1 = str(a).find("-id=\"")
                    i2 = str(a).find("\" data-signup")
                    reviewID = str(a)[i1 + 5:i2]
                    
                    dt = a.find("span", class_="rating-qualifier")
                    date = str(dt.string)
                    date = date.strip()
                    
                    rt = a.find("div", class_="i-stars")
                    rating = str(rt['title'])
                    
                    counts = a.find_all("span", class_="count")
                    i1 = str(counts[0]).find(">")
                    i2 = str(counts[0]).find("</")
                    usefulCount = str(counts[0])[i1 + 1: i2]
                    if(usefulCount == ''):
                        usefulCount = "0"
                    i1 = str(counts[1]).find(">")
                    i2 = str(counts[1]).find("</")
                    funnyCount = str(counts[1])[i1 + 1: i2]
                    if(funnyCount == ''):
                            funnyCount = "0"
                    i1 = str(counts[2]).find(">")
                    i2 = str(counts[2]).find("</")
                    coolCount = str(counts[2])[i1 + 1: i2]
                    if(coolCount == ''):
                        coolCount = "0"
                                
                    csv.write(reviewID + "," + businessID + "," + reviewerID + "," + date + "," + rating + "," + usefulCount + "," + coolCount + "," + funnyCount + "\n")
            
                respage = respage + 20
                resfull = res1st + res2nd + res3rd + str(respage) + res4th
                RestaurantPage = urllib.request.urlopen(resfull).read()
                RestaurantSoup = BeautifulSoup(RestaurantPage, "html.parser")
                Reviews = RestaurantSoup.find_all("div", class_="review review--with-sidebar")


    Page = Page + 10
    full = firsthalf + str(Page) + secondhalf
    YelpPage = urllib.request.urlopen(full).read()
    soup = BeautifulSoup(YelpPage, "html.parser")
    resultarr = soup.find_all("li", class_="regular-search-result")
