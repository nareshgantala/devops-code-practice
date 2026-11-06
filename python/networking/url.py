import urllib.parse

url = "https://www.google.com/search?q=python"
parsed_url = urllib.parse.urlparse(url)
print("Scheme:", parsed_url.scheme)
print("Netloc:", parsed_url.netloc)
print("Path:", parsed_url.path)
print("Query:", parsed_url.query)
print("Fragment:", parsed_url.fragment)
