import requests

import re

# = "http://books.toscrape.com/"

def fetch(url):

    response = requests.get(url)

    assets = re.findall('<img src="([^"]+)"', str(response.content))

    links = re.findall('<a href="([^"]+)"', str(response.content))

    return(assets, links)

def getWebsiteAssets(urls):

    for url in urls:

        print(fetch(url))

if __name__ == "__main__":

    urls = list(map(str,input("\nEnter the urls : ").strip(',').split()))

    getWebsiteAssets(urls)