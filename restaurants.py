#
# Corey Habel - chabel2
#
#

from bs4 import BeautifulSoup
import urllib.request
import csv
import string

#
# insert code to iterate through each restaurant page in the search results
#


r = urllib.request.urlopen('https://www.yelp.com/biz/lowcountry-south-loop-chicago?frvs=True').read()
soup = BeautifulSoup(r, 'html.parser')


with open('restaurant.csv', 'w', newline='') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  csvwriter.writerow(['restaurantID', 'name', 'location', 'reviewCount', 'rating'])



  name = soup.find(class_='biz-page-title embossed-text-white').text.strip()

  # location
  location = soup.find(class_='street-address').text.strip()

  # reviews
  reviews = soup.find(class_='review-count rating-qualifier').text.strip()
  reviewCount = reviews.strip(string.ascii_letters)

  # rating
  ratingDiv = soup.find(class_='i-stars i-stars--large-4-half rating-very-large')
  rating = ratingDiv.find('img')['alt'].strip(string.ascii_letters)

  # categories
  categoriesDiv = soup.find(class_='category-str-list')
  categoriesList = categoriesDiv.find_all('a')

  categories = []
  for category in categoriesList:
    categories.append(category.text)

  # address
  address = soup.find(class_='street-address').text.strip()


  csvwriter.writerow([game, year, winner, score, loser, venue])


  print(categories)
  

