#
# Corey Habel - chabel2
#
#

from bs4 import BeautifulSoup
import urllib.request
import csv
import string

reviewID = ""
businessID = ""
reviewerID = ""
date = ""
#reviewContent
rating = ""
usefulCount = ""
#coolCount
#funnyCount
Page = 0

firsthalf = "https://www.yelp.com/search?find_loc=60605&start="
secondhalf = "&cflt=restaurants"
full = firsthalf + str(Page) + secondhalf

YelpPage = urllib.request.urlopen(full).read()
soup = BeautifulSoup(YelpPage, "html.parser")

resultarr = soup.find_all("li", class_="regular-search-result")
                                    

with open('restaurant.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['name', 'location', 'reviewCount', 'rating', 'categories', 'address', 'GoodforKids'])

    while(len(resultarr) != 0):
        
        for i in resultarr:
            
            address = str(i.address)
            
            if "60605" not in address:
                continue
                
            else:

                a = str(i.find("a", class_="biz-name js-analytics-click"))
                i1 = a.find("biz/")
                i2 = a.find("True\"")
                res1st = "https://www.yelp.com"
                res2nd = a[i1 - 1:i2 + 4]
                res3rd = "?start="
                respage = 0
                res4th = "&sort_by=date_asc"
                resfull = res1st + res2nd + res3rd + str(respage) + res4th
                businessID = a[i1 + 4: i2 - 6]
                #print(resfull)
                RestaurantPage = urllib.request.urlopen(resfull).read()
                RestaurantSoup = BeautifulSoup(RestaurantPage, "html.parser")

                #################
                #
                # Data Extraction
                #
                # TODO: restaurantID, Hours, GoodFor

                name = "N/A"
                location = "N/A"
                reviewCount = "N/A"
                rating = "N/A"
                categories = "N/A"
                address = "N/A"
                goodForKids = "N/A"
                acceptsCreditCards = "N/A"
                parking = "N/A"
                attire = "N/A"
                goodForGroups = "N/A"
                priceRange = "N/A"
                takesReservations = "N/A"
                delivery = "N/A"
                takeout = "N/A"
                waiterService = "N/A"
                outdoorSeating = "N/A"
                wifi = "N/A"
                alcohol = "N/A"
                NoiseLevel = "N/A"
                ambience = "N/A"
                hasTV = "N/A"
                caters = "N/A"
                wheelchairAccessible  = "N/A"
                website = "N/A"
                phoneNumber = "N/A"

                # name
                name = RestaurantSoup.find('h1').text.strip()
                print(name)
                
                # location
                location = RestaurantSoup.find(class_='street-address').text.strip()

                # reviews
                reviews = RestaurantSoup.find(class_='review-count rating-qualifier').text.strip()
                reviewCount = reviews.strip(string.ascii_letters)

                # rating
                ratingDiv = RestaurantSoup.find(class_='biz-rating biz-rating-very-large clearfix')
                rating = ratingDiv.find('img')['alt'].strip(string.ascii_letters)

                # categories
                categoriesDiv = RestaurantSoup.find(class_='category-str-list')
                categoriesList = categoriesDiv.find_all('a')

                categories = []
                for category in categoriesList:
                  categories.append(category.text)

                # address
                address = RestaurantSoup.find(class_='street-address').text.strip()

                # hours
                # TODO

                # short def list
                defList1 = RestaurantSoup.find(class_='short-def-list')
                defList2 = defList1.find_next(class_='short-def-list')
                defList3 = defList2.find_next(class_='short-def-list')

                #print(defList)

                if defList3 is None:
                    dl_list = defList2.find_all("dl")
                elif deflist2 is None:
                    dl_list = defList1.find_all("dl")
                else:
                    dl_list = defList3.find_all("dl")
                

                for dl in dl_list:
                    dt = dl.find("dt")

                    

                    if "Accepts Credit Cards" in dt.text:
                        # Accepts Credit Cards
                        acceptsCreditCards = dt.find_next("dd").text.strip()

                    if "Parking" in dt.text:
                        # Parking
                        parking = dt.find_next("dd").text.strip()
                    
                    if "Good for Kids" in dt.text:
                        # Good for Kids
                        goodForKids = dt.find_next("dd").text.strip()
                    
                    if "Attire" in dt.text:
                        # Attire
                        attire = dt.find_next("dd").text.strip()

                    if "Good for Groups" in dt.text:
                        # Good for Groups
                        goodForGroups = dt.find_next("dd").text.strip()

                    if "Takes Reservations" in dt.text:
                        # Takes Reservations
                        takesReservations = dt.find_next("dd").text.strip()

                    if "Delivery" in dt.text:
                        # Delivery
                        delivery = dt.find_next("dd").text.strip()

                    if "Take-out" in dt.text:
                        # Takeout
                        takeout = dt.find_next("dd").text.strip()

                    if "Waiter Service" in dt.text:
                        # Takes Reservations
                        waiterService = dt.find_next("dd").text.strip()

                    if "Outdoor Seating" in dt.text:
                        # Outdoor Seating
                        outdoorSeating = dt.find_next("dd").text.strip()

                    if "Wi-Fi" in dt.text:
                        # WiFi
                        wifi = dt.find_next("dd").text.strip()

                    if "Alcohol" in dt.text:
                        # Alcohol
                        alcohol = dt.find_next("dd").text.strip()

                    if "Noise Level" in dt.text:
                        # Noise Level
                        NoiseLevel = dt.find_next("dd").text.strip()

                    if "Ambience" in dt.text:
                        # Ambience
                        ambience = dt.find_next("dd").text.strip()

                    if "Has TV" in dt.text:
                        # Has TV
                        hasTV = dt.find_next("dd").text.strip()

                    if "Caters" in dt.text:
                        # Caters
                        caters = dt.find_next("dd").text.strip()

                    if "Wheelchair Accessible" in dt.text:
                        # Wheelchair Accessible
                        wheelchairAccessible = dt.find_next("dd").text.strip()

                    if "Takes Reservations" in dt.text:
                        # Takes Reservations
                        takesReservations = dt.find_next("dd").text.strip()


                # price range
                priceRange = RestaurantSoup.find(class_='nowrap price-description')
                if priceRange is None:
                    priceRange = "N/A"
                else:
                    priceRange = RestaurantSoup.find(class_='nowrap price-description').text.strip()
                
                # Website
                site = RestaurantSoup.find("span", text="Business website")

                if site is None:
                    website = "N/A"
                else:
                    website = site.find_next("a").text.strip()

                # phone number
                phoneNumber = RestaurantSoup.find(class_='biz-phone')
                if phoneNumber is None:
                    phoneNumber = "N/A"
                else:
                    phoneNumber = RestaurantSoup.find(class_='biz-phone').text.strip()

                csvwriter.writerow([name, location, reviewCount, rating, categories, address, 
                                    goodForKids, acceptsCreditCards, parking, attire, goodForGroups, 
                                    priceRange, takesReservations, delivery, takeout, waiterService, 
                                    outdoorSeating, wifi, alcohol, NoiseLevel, ambience, hasTV, caters, 
                                    wheelchairAccessible, website, phoneNumber])


        Page = Page + 10
        full = firsthalf + str(Page) + secondhalf
        YelpPage = urllib.request.urlopen(full).read()
        soup = BeautifulSoup(YelpPage, "html.parser")
        resultarr = soup.find_all("li", class_="regular-search-result")
