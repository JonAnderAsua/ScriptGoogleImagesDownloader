import json

with open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/ladonacion.es/entities.json", "r") as e:
    entitateak = json.load(e)

with open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/ladonacion.es/persons.json", "r") as pe:
    pertsonak = json.load(pe)

with open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/ladonacion.es/places.json", "r") as pl:
    lekuak = json.load(pl)

f = open("/home/jonander/PycharmProjects/ScriptGoogleImagesDownloader/nombres.txt",'w')

for i in pertsonak['persons']:
    f.write(i['title'] + '\n')

for j in entitateak['entities']:
    f.write(j['title'] + '\n')

for u in lekuak['places']:
    f.write(u['title'] + '\n')