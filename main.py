from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

f = open('/home/jonander/PycharmProjects/ScriptGoogleImagesDownloader/nombres.txt','r')

arguments = {"keywords":'alexelcapo',"limit":1,"print_urls":True}
paths = response.download(arguments)
