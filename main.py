from google_images_download import google_images_download  as gi #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Mariano Rajoy","limit":1,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

if __name__ == '__main__':
    paths = response.download(arguments)  # passing the arguments to the function
    print(paths)  # printing absolute paths of the downloaded images
