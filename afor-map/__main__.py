from pathlib import Path

import progress.bar

from .loaders import CSV
from .models import Node
from .services import GEODecoder

DATA_PATH = Path("data")
OUTPUT_PATH = Path("output")

csv_loader = CSV(delimiter="\t", quotechar='"')
geo_locator = GEODecoder(language="it")

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
