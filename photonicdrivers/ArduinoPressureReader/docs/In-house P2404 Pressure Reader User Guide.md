P2404 – Trykaflæser over Ethernet

Denne boks er lavet til at aflæse op til 4 trykmålere (VPL-16N) over en ethernet port

### Tilslutning

Boksen skal forsynes af 24V center positiv 5.5/2.1mm barrel. 0.5A minimum.
Denne strømforsyning forsyner også trykmålerne.
For at tilslutte en trykmåler skrues skuerne af den ende UDEN stik og derfra kan det løse låg trækkes ud. Der sidder 4 skrueterminaler, en til hver sensor. På sensoren skal de forbindes til Uout (forbindes til ”in” på printet), 24V og 0V

### Brug

Trykmålerne bliver samplet af en Arduino og bliver delt ned med en faktor 2 undervejs.
Det er en 10bit adc, det vil sige at en adc kode på 1023 svare til en måling på 10V og en på 511 svare til 5V

Måleren aflæses hvad at sende en http-request til dens IP adresse, hvor den så svarer med en JSON streng med en adc aflæsning for de 4 kanaler:

{

"channel": [

0,

0,

0,

0

]

}

Dette kan læses fra en computer med følgende Python kode:

from urllib.request import urlopen

import json

url = "http://10.205.64.111/"

while 1:

data = json.loads(urlopen(url).read())

print (data["channel"][0])

print (data["channel"][1])

print (data["channel"][2])

print (data["channel"][3])

time.sleep(1)