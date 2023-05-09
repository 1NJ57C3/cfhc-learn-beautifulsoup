# Separate organizational thing(s) / House-keeping
import os
from config.definitions import PARENT_DIR

# Tutorial modules
from bs4 import BeautifulSoup
from urllib import request # Using native fetch library instead of third-party
import requests

with open(os.path.join(PARENT_DIR, 'Beautiful-Soup-Tutorial', 'index.html'), "r") as file:
  doc = BeautifulSoup(file, "html.parser")

print(doc.prettify()) # Pretty-prints (adds nesting indents to) HTML file BeautifulSoup method, not native, only works on single [parent] element

# Finding a tag by name
tag = doc.title # Returns first matching tag (title, in this case)
tag.string = 'innerText' # Edit innerText of tag
print(tag)

# Finding multiple tags by name
tags = doc.find_all("p") # Returns list of matches
print(tags)

# Accessing tags using `find_all()`
tags = doc.find_all("p")[0]
print(tags.find_all("b")[1].i)

url = "https://www.newegg.com/evga-geforce-rtx-3080-ti-12g-p5-3967-kr/p/N82E16814487547"

# # # From official Python [documentation](https://docs.python.org/3/howto/urllib2.html)
# # req = request.Request(url) # This step appears to be extraneous for simple GET
# # with request.urlopen(req) as response:
# #   doc = response.read()
# # print(BeautifulSoup(doc, "html.parser").prettify())

# response = request.urlopen(url) # Successful attempt at trimming the "fat"
# print(BeautifulSoup(response, "html.parser").prettify())

# The fetch method from video for science -- same result
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$") # Attempt to find tag containing price
parent = prices[0].parent # Parent of first search result
print(parent) # Confirm contents of parent
strong = parent.find("strong") # Find "strong" tag after visually confirming correct price on webpage
print(strong.string) # Print price

# price = parent.strong.string + parent.sup.string
# print(price) # Actual price