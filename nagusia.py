# from simple_image_download import Downloader, simp
from simple_image_download.simple_image_download import Downloader, simp

response = simp.simple_image_download()
response.download('bear supermario', limit=5)