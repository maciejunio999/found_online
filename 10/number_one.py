
import requests 
from PIL import Image 
  
url = 'https://stooq.pl/c/?s=eurpln&d=20240110&c=1d&t=l&a=ln'

try:
    if not (url.startswith('https://') or url.startswith('http://')):
        raise requests.exceptions.MissingSchema
except requests.exceptions.MissingSchema:
    er = 'There is no schema suppied, it douesnt start with https:// or http://'
    print(er)

  
# This statement requests the resource at 
# the given link, extracts its contents 
# and saves it in a variable
try:
    if url.startswith('https://') or url.startswith('http://'):
        data = requests.get(url).content
except requests.exceptions.ConnectionError:
    er = 'There is nothing under this URL.'
    print(er)
  
# Opening a new file named img with extension .jpg 
# This file would store the data of the image file 
f = open('img.jpg','wb') 

try:
    # Storing the image data inside the data variable to the file
    f.write(data) 
    f.close() 
    
    # Opening the saved image and displaying it 
    img = Image.open('img.jpg')

    try:
        img.show()
    except ValueError:
        print('Under this URL there is no image.')
except NameError as err:
    print(er)