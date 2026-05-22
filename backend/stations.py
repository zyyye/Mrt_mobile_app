import requests
import xml.etree.ElementTree as ET
from .config import STATION_XML_URL

def load_station_map():
    response = requests.get(STATION_XML_URL)
    root = ET.fromstring(response.content)

    station_map = {}

    for stop in root.findall(".//mrtStop"):
        name = stop.text.strip()
        value = stop.attrib["value"]

        station_id = int(value.split("_")[0])
        clean_name = name.split("(")[0].strip()

        station_map[clean_name] = station_id

    return station_map