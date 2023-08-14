from bs4 import BeautifulSoup
import requests
import csv

"""Scrape the Billboard Japan Hot 100"""

url = 'https://www.billboard.com/charts/japan-hot-100/'

# Get the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Open a file to write the data to
file = open('billboard_japan_hot_100.csv', 'w')
writer = csv.writer(file)

# CSV Headers
writer.writerow(['Rank', 'Title', 'Artist', 'Last Week', 'Peak', 'Weeks on Chart'])

# Loop through the chart rows and get their song data
rows = soup.find_all('div', attrs={'class':'o-chart-results-list-row-container'})

for row in rows:
    rank = row.li.get_text(strip=True)
    title = row.find('h3', attrs={'id':"title-of-a-story"}).get_text(strip=True)
    artist = row.h3.find_next('span').get_text(strip=True)
    prev_week = row.h3.find_next('span').find_next('span').get_text(strip=True)
    peak = row.h3.find_next('span').find_next('span').find_next('span').get_text(strip=True)
    weeks = row.h3.find_next('span').find_next('span').find_next('span').find_next('span').get_text(strip=True)
    writer.writerow([rank, title, artist, prev_week, peak, weeks]) # Write data to CSV
    print(rank, title, artist, prev_week, peak, weeks, sep=' | ') # Print data to console

file.close()