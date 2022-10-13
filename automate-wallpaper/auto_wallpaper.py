""" Problem:
    Download and change desktop wallpapers automatically
"""
import requests
import json
import PyWallpaper

api_url0 = "https://apod.nasa.gov/apod/image/2209/WR140_WebbSchmidt_960.jpg"
api_url = "https://cdn.searchenginejournal.com/wp-content/uploads/2019/08/c573bf41-6a7c-4927-845c-4ca0260aad6b-760x400.jpeg"

# get the json
response = requests.get(api_url0)
content = response.content.decode('UTF-8')

#convert string to json
dict_content = json.loads(content)

#get the image url
image_url = dict_content['url']

#download the image
res = requests.get(image_url)

#save the image
with open('apod.png', 'wb') as image:
    image.write(res.content)

#set as wallpaper
PyWallpaper.change_wallpaper('apod.png')



