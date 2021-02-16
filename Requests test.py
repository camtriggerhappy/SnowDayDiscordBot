import requests
import xml.etree.ElementTree as ET

r = requests.get("http://wvde.state.wv.us/closings/xml/putnam")
Tree = ET.fromstring(r.text)
for node in Tree:
    for child in node:
        print(child.text)


#print(r.text)
