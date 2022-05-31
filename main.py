from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

f = open('./nombres.txt','r',encoding='utf-8')

for linea in f:
    arguments = {"keywords":linea,"limit":1,"print_urls":True}
    paths = response.download(arguments)
