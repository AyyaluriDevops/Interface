# Interface

This is a webcrawler program in python. It fetches <img> tag urls and <a> tag urls from the provided list of urls.
Python modules used:
  1) request 
  2) requests
Python function:
  1) fetch(url):
      Gets the response content of the url passed and find all the 'img' and 'a' tag urls (assets/links)
      Returns object containing assets amd links

  2) getWebsiteAssets(url):
      Gets the individual url's from the list of urls provided
      Calls fetch(url)
  
