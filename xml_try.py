import xmltodict

import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

pars = xmltodict.parse(xml)
print(pars['osm']['node'][100]['@id'])