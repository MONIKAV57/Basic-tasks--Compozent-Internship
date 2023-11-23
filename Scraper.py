# Import the required modules
import requests
from bs4 import BeautifulSoup
from os.path import basename
import os


# Get the URL of the website from the user
url = input("Enter the URL of the website: ")


# Get the HTML content of the website
response = requests.get(url)
html = response.text


# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")


# Find all the image tags
images = soup.find_all("img")


# Create a folder named "images" to store the downloaded images
if not os.path.exists("images"):
    os.mkdir("images")


# Loop through the images and download them
for image in images:
    # Get the image source URL
    src = image["src"]


   # Download the image and save it to the "images" folder
    with open("images/" + basename(src), "wb") as f:
        f.write(requests.get(url+src).content)


# Print a message when done
print("All images downloaded!")
