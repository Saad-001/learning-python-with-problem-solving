import json

import PyWallpaper
from requests import get

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = get(api_url)
content = response.content.decode("UTF-8")

main_content = json.loads(content)

img_url = main_content["url"]

img_res = get(img_url)

with open("wallpaper.png", 'wb') as image :
    image.write(img_res.content)

PyWallpaper.change_wallpaper("F:\learning python\wallpaper.png")
