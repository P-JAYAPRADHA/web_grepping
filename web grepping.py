"""
import requests
import re
from bs4 import BeautifulSoup

# Send a GET request to the target web page
url = 'https://www.iana.org/domains/reserved'
response = requests.get(url)

# Search for the word "example" within the raw HTML content using regular expressions
pattern = 'IANA'
matches = re.findall(pattern, response.text)

# If the word is not found in the raw HTML content, parse the HTML using Beautiful Soup and search for the word in the parsed HTML tree
if not matches:
    soup = BeautifulSoup(response.text, 'html.parser')
    matches = soup.find_all(string='example')

# Print all the matches found
if matches:
    print('Found the following matches:')
    for match in matches:
        print(match)
else:
    print('Did not find any matches.')

"""

import requests
from bs4 import BeautifulSoup

# Send a GET request to the target web page
url = 'https://www.iana.org/domains/reserved'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the fourth paragraph
paragraphs = soup.find_all('p')
print(paragraphs[1])
if len(paragraphs) >= 4:
    fourth_paragraph = paragraphs[1]
    
else:
    print('Could not find the specified paragraph.')

