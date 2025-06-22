import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://layla.ai'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get HTML
html = soup.prettify()
print("HTML:\n", html)

# Get linked CSS files
css_links = [urljoin(url, link['href']) for link in soup.find_all('link', rel='stylesheet')]

print("\nCSS Files:")
for css_url in css_links:
    try:
        css_response = requests.get(css_url)
        print(f"\n---- CSS from {css_url} ----\n")
        print(css_response.text[:1000])  # Print first 1000 chars
    except Exception as e:
        print(f"Error fetching CSS from {css_url}: {e}")
