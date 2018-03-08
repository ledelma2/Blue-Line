
from bs4 import BeautifulSoup
import urllib.request
import csv
import string


r = urllib.request.urlopen('https://www.yelp.com/biz/lowcountry-south-loop-chicago?frvs=True').read()
soup = BeautifulSoup(r, 'html.parser')


# table = soup.find('table')
# table = table.find_next('table')

# table_rows = table.find_all('tr')

with open('restaurant.csv', 'w', newline='') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  csvwriter.writerow(['restaurantID', 'name', 'location', 'reviewCount', 'rating'])



  name = soup.find(class_='biz-page-title embossed-text-white').text.strip()

  location = soup.find(class_='street-address').text.strip()

  reviews = soup.find(class_='review-count rating-qualifier').text.strip()
  reviewCount = reviews.strip(string.ascii_letters)

  ratingDiv = soup.find(class_='i-stars i-stars--large-4-half rating-very-large')
  rating = ratingDiv.find('img')['alt'].strip(string.ascii_letters)

  categoriesDiv = soup.find(class_='category-str-list')
  categoriesList = categoriesDiv.find_all('a')

  categories = []
  for category in categoriesList:
    categories.append(category.text)

  print(categories)
  

  

  # for row in table_rows:
    # cells = row.find_all('td')

    # if len(cells) > 0:

      # game (numeral)
      # game = cells[0].find('a').text

      # date (year)
      # year = cells[1].find('span')
      # year = year.find_next('span').text
      # year = year[len(year) - 4:]

      # winning team
      # winner = cells[2].find('span').text.rstrip(' !')

      #score
      # score = cells[3].find(class_='sorttext').text

      # loser
      # loser = cells[4].find('span').text.rstrip(' !')

      # venue
      # venue = cells[5].find('span').text.rstrip(' !')

      
      # write line to csv file
      # if (len(score) != 1):
       #  csvwriter.writerow([game, year, winner, score, loser, venue])
  

