# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 18:28:15 2018
@author: Duong Le
@credit: Liam
"""

from bs4 import BeautifulSoup
import urllib.request


#set up url
Page = 0
firsthalf = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=60605&start="
full = firsthalf + str(Page)

#list of author
Authors=[]

#total restaurant
total=0
authorsTotal=0

while(total<100):
    #get html content of the search result
    print("This is the url: "+full,end='\n')
    YelpPage = urllib.request.urlopen(full).read()
    soup = BeautifulSoup(YelpPage, "html.parser")
    items=soup.findAll(class_="regular-search-result")  

    #stop the loop if there is no more result for the search query     
    if(len(items) == 0):
       # print("HERE")
        break
    
    #get the author information for each restaurant
    for restaurant in items:        
        reviews=restaurant.find(class_='review-count rating-qualifier')        
        count=0
        for reviewCount in reviews:
            for num in reviewCount.split():
                if(num.isdigit()):
                    count=num
                    break
        rAddress=restaurant.find('address')
       
        #filter the restaurant that meets the requirement: within 60605 and have at least 20 reviews
        if(int(count)>19 and rAddress is not None and ('60605' in rAddress.text)):
            total+=1
        
            #get html content of individual restaurant page        
            rID=restaurant.find('a')['href']
            newLink="https://www.yelp.com"+rID   
            newYelpPage=urllib.request.urlopen(newLink).read()
            soup=BeautifulSoup(newYelpPage, "html.parser")
            authorSearchResult=soup.find(class_='ylist ylist-bordered reviews')
            authorInfo=[]

            rID=rID[5:rID.index('?')]
            print("<<RESTAURANT "+rID+">>") 
            authorsTotal=0
            #get the inforamtion for each author that wrote review in the restaurant
            for author in authorSearchResult.find_all('div', class_='review review--with-sidebar'):  
                authorsTotal=authorsTotal+1              
                uID='' 
                uName=''
                uLocation=''
                uViewCount='0'
                uFriendCount='0'
                uPhotoCount='0'            

                userObj=author.find('a', class_='user-display-name js-analytics-click')  
                if(userObj is not None):
                    link=userObj['href']
                    uID=link[(link.index('=')+1):]                    
                    uName=userObj.text
                
                locationObj=author.find('li',class_='user-location responsive-hidden-small')
                if(locationObj is not None):
                    uLocation= locationObj.find('b').text
                
                viewCountObj=author.find('li',class_='review-count responsive-small-display-inline-block')
                if(viewCountObj is not None):
                    uViewCount=viewCountObj.find('b').text
                
                friendCountObj=author.find('li',class_='friend-count responsive-small-display-inline-block')
                if(friendCountObj is not None):
                    uFriendCount=friendCountObj.find('b').text
                
                photoCountObj=author.find('li',class_='photo-count responsive-small-display-inline-block')
                if(photoCountObj is not None):
                    uPhotoCount=photoCountObj.find('b').text
                authorInfo.append(rID)
                authorInfo.append(uID)
                authorInfo.append(uName)
                authorInfo.append(uLocation)
                authorInfo.append(uViewCount)
                authorInfo.append(uFriendCount)
                authorInfo.append(uPhotoCount) 
                Authors.append(authorInfo)
                print("ReviewNum "+str(authorsTotal)+" "+ str(authorInfo))
                authorInfo=[]            
            #print(total)
    #update url for search query
    Page=Page+10
    full = firsthalf + str(Page)

print("total restaurant " + str(total))
print(len(Authors))

                    
                


 


    

   

# while(len(resultarr) != 0):
#     for i in resultarr:
#         address = str(i.address)
#         if "60605" not in address:
#             continue
#         else:
#             tot = tot + 1
#             print(tot)
#     Page = Page + 10
#     full = firsthalf + str(Page) + secondhalf
#     YelpPage = urllib.request.urlopen(full).read()
#     soup = BeautifulSoup(YelpPage, "html.parser")
#     resultarr = soup.find_all("li", class_="regular-search-result")