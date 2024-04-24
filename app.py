from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('tv-no-signal-color-bars-150-colorswall - Copy.png')) 
hash1 = imagehash.average_hash(Image.open('tv-no-signal-color-bars-150-colorswall.png')) 
cutoff = 5  # maximum bits that could be different between the hashes. 

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')