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


nodes_path = Path("data/nodes_fixed.csv")
nodes = csv_loader.read(nodes_path, Node)

for node in nodes:
    print(node)
