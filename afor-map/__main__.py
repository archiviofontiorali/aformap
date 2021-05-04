import csv
import dataclasses
import time
from pathlib import Path

import geopy
import progress.bar


@dataclasses.dataclass
class Node:
    id: str
    video_id: str
    name: str
    address: str
    description: str

    latitude: float = None
    longitude: float = None


class CSV:
    def __init__(self, **opts):
        self._opts = opts

    def read(self, path, model, skip_header=True) -> list:
        with open(path, "rt") as fp:
            reader = csv.reader(fp, **self._opts)
            if skip_header:
                next(reader)
            return [model(*row) for row in reader]

    def write(self, path, header, objs, write_header=True):
        with open(path, "wt") as fp:
            writer = csv.writer(fp, **self._opts)

            if write_header:
                writer.writerow(header)

            for obj in objs:
                row = [getattr(obj, h) for h in header]
                writer.writerow(row)


class GEOLocator:
    def __init__(self):
        self._language = "it"
        self._user_agent = "aformap/v0.1.0"
        self._locator = geopy.geocoders.Nominatim(user_agent=self._user_agent)

    def geocode(self, address) -> (float, float):
        location = self._locator.geocode(address, language=self._language)
        latitude = getattr(location, 'latitude', None)
        longitude = getattr(location, 'longitude', None)
        time.sleep(1)  # Ensure 1 second is passed
        return latitude, longitude


DATA_PATH = Path("data")
OUTPUT_PATH = Path("output")

csv_loader = CSV(delimiter="\t", quotechar='"')
geo_locator = GEOLocator()

# Read nodes
nodes_path = DATA_PATH / "nodes_fixed.csv"
nodes = csv_loader.read(nodes_path, Node)

# Convert address to coordinates
bar = progress.bar.IncrementalBar("Geocoding...", max=len(nodes))
for node in nodes:
    if node.address:
        node.latitude, node.longitude = geo_locator.geocode(node.address)
    bar.next()
else:
    bar.finish()

# Save nodes with coordinates
geocoded_path = OUTPUT_PATH / "nodes_geocoded.csv"
geocoded_header = [
    "id",
    "video_id",
    "name",
    "address",
    "description",
    "latitude",
    "longitude",
]
geocoded_nodes = filter(lambda n: n.latitude is None or n.longitude is None, nodes)
csv_loader.write(geocoded_path, geocoded_header, geocoded_nodes)
