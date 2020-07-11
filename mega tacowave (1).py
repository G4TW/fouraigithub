#@title
!git clone https://github.com/jeroenmeulenaar/python3-mega.git
!(cd python3-mega; pip install urlobject pycrypto)
 
import os
os.chdir('python3-mega')
from mega import Mega
os.chdir('../')
m = Mega.from_ephemeral()
print("Downloading Dictionary...")
m.download_from_url('https://mega.nz/#!yAMyFYCI!o_UmixbiIzosyYk-6O5xRZZDGpFRik_eMrZum-iQuhQ')
