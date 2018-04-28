from pprint import pprint
import string
from PIL import Image
import numpy as np
import requests
from io import BytesIO

class ASCII():
   
  def __init__(self, img_path, name='ascii'):
       
    self.img_path = img_path
    self.name = name
    self.ascii_map = ['@', '%', '#', 'x', '+', '=', ':', '-', '.', ' ']
    self.categorize_img_path()

  def categorize_img_path(self):

    if "http" in self.img_path:
      image = Image.open(BytesIO(requests.get(self.img_path).content)).convert('L')
    else:
      image = Image.open(self.img_path).convert('L')

    gif = ".gif" in self.img_path
    
    self.preprocess_image(image, gif)
  
  def preprocess_image(self, image, gif):
    
    basewidth = 200
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    image = image.resize((basewidth,hsize), Image.ANTIALIAS)
    image.show()
    if not gif:
      image_array = np.array(image)
    
    self.make_ASCII(image_array, gif)

  def make_ASCII(self, image_array, gif):

    f = open(self.name+".txt","w+")
     
    for row in range(len(image_array)): 
      if row % 2 == 0:
        ascii_row = ""
        for col in image_array[row]:
          ascii_row += self.ascii_map[int(col/26)]
        f.write(ascii_row+"\n")

    f.close()


gioconda = ASCII("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/687px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg", "gioconda")
