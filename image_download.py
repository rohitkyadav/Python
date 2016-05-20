import random
import urllib.request
def download_img(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpeg"
    urllib.request.urlretrieve(url,full_name)
download_img("https://upload.wikimedia.org/wikipedia/commons/b/b4/JPEG_example_JPG_RIP_100.jpg")








