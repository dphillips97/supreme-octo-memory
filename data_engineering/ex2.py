'''
Goals
1. Scrape contents of given url
2. Download file on line with timestamp "2024-01-19 10:27"
3. Open file with pandas and find records with highest hourly DryBulbTemperature
4. Print to terminal
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
SEARCH_STRING = '2024-01-19 10:27'

def main():

    # Call URL and save as text object
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')


    # Find <td> that contains SEARCH_STRING
    # Navigate to parent <tr>
    # Loop thru <td>
    # Get csv name

    '''
    Many instances at this timestamp (260+).
    Not sure which one to get.
    Filesize increases to 45MB and file index number also increases
    But larger files don't necessarily have the hightest name.
    '''
    td_dates = soup.find_all("td", string=re.compile(SEARCH_STRING))

    

if __name__ == "__main__":
    main()