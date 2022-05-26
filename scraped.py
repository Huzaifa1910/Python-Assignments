## Web scraping
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

def get_links(date):
    # Parse the page into a Beautiful Soup object
    page = urlopen('https://www.nba.com/games?date={}'.format(date))
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html,  "html.parser")
    # Find all a elements with box score links
    links = soup.find_all('a', {'data-id':'nba:games:main:box-score:cta'})
    # Get and return the list of links 
    full_links = list()
    for box_score in links:
       full_links.append(urllib.parse.urljoin('https://www.nba.com', box_score['href']))
    
    return full_links
dated = "2021-01-18"
get_links(dated)
