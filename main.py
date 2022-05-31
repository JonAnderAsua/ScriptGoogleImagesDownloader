from google_images_download import google_images_download
import unidecode

response = google_images_download.googleimagesdownload()

f = open('./nombres.txt','r',encoding='utf-8')

for linea in f:
    print(linea)
    arguments = {"keywords":unidecode.unidecode(linea),"limit":1,"print_urls":True}
    paths = response.download(arguments)
