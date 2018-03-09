# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:15 2018
@author: Duong Le
@credit: Liam
"""

from bs4 import BeautifulSoup
import urllib.request

csv.write("reviewID, businessID, reviewerID, date, reviewContent, rating, usefulCount, coolCount, funnyCount\n")


Page = 0
firsthalf = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=60605&start="
full = firsthalf + str(Page)
restaurantID = []
total=0

while(total<10):
    print("This is the url: "+full,end='\n')
    YelpPage = urllib.request.urlopen(full).read()
    soup = BeautifulSoup(YelpPage, "html.parser")
    items=soup.findAll(class_="regular-search-result")    
    for restaurant in items:
        rID=restaurant.find('a')['href']
        reviews=restaurant.find(class_='review-count rating-qualifier')        
        count=0
        for reviewCount in reviews:
            for num in reviewCount.split():
                if(num.isdigit()):
                    count=num
                    break
        
        rID=restaurant.find('a')['href']
        #go to each page
        if(int(count)>19):
            restaurantID.append(rID)
            newLink="https://www.yelp.com"+rID
            print(newLink)
            newYelpPage=urllib.request.urlopen(newLink).read()
            soup=BeautifulSoup(newYelpPage, "html.parser")
            authorItems=soup.find(class_='ylist ylist-bordered reviews')
            for author in authorItems.find_all('li'):
                userID=author.find(class_='user-display-name js-analytics-click')
                print(userID)

 


    

   

